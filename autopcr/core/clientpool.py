from .pcrclient import pcrclient
from .apiclient import apiclient, ApiException
from .sdkclient import sdkclient
from .datamgr import datamgr
from .sessionmgr import sessionmgr
from .misc import errorhandler, mutexhandler
from .base import Component, Request, TResponse, RequestHandler
from ..model.sdkrequests import ToolSdkLoginRequest
from typing import Dict, Tuple, Set
from ..constants import SESSION_ERROR_MAX_RETRY, CLIENT_POOL_SIZE_MAX, CLINET_POOL_MAX_AGE
import time

class PreToolSdkLoginRequestHandler(Component[apiclient]):
    def __init__(self, pool: 'ClientPool'):
        self.pool = pool
    async def request(self, request: Request[TResponse], next: RequestHandler) -> TResponse:
        assert isinstance(self._container, PoolClientWrapper)
        if isinstance(request, ToolSdkLoginRequest):
            self._container.uid = request.uid
            self.pool._on_sdk_login(self._container)

class SessionErrorHandler(Component[apiclient]):
    def __init__(self, pool: 'ClientPool'):
        self.pool = pool
        self.retry = 0
    async def request(self, request: Request[TResponse], next: RequestHandler) -> TResponse:
        assert isinstance(self._container, PoolClientWrapper)
        try:
            return await next.request(request)
        except ApiException as e:
            if e.result_code == 6002 and self.retry < SESSION_ERROR_MAX_RETRY:
                self.retry += 1
                self._container.session.clear_session()
                return await self.request(request, next)
            raise
        finally:
            self.retry = 0

class PoolClientWrapper(pcrclient):
    def __init__(self, pool: 'ClientPool', sdk: sdkclient):
        apiclient.__init__(self, sdk)
        self.keys = {}
        self.data = datamgr()
        self.session = sessionmgr(sdk)
        self.pool = pool
        self.uid: str = None
        self.register(errorhandler())
        self.register(self.data)
        self.register(PreToolSdkLoginRequestHandler(pool))
        self.register(self.session)
        self.register(SessionErrorHandler())
        self.register(mutexhandler())

    async def __aenter__(self):
        self.keys.clear()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.pool._put_in_pool(self)

class ClientCache:
    def __init__(self, client: PoolClientWrapper):
        self.client = client
        self.last_access = int(time.time())

class ClientPool:
    def __init__(self):
        self.active_uids: Set[str] = set()
        self._pool: Dict[Tuple[str, str], ClientCache] = dict()

    def _on_sdk_login(self, client: PoolClientWrapper):
        if client.uid in self.active_uids:
            raise RuntimeError('用户的另一项请求正在进行中')
        self.active_uids.add(client.uid)

    def _put_in_pool(self, client: PoolClientWrapper):
        if client.uid not in self.active_uids: # client disposed without being logged in
            return
        if not client.logged: # client session expired and not successfully recovered
            return
        self.active_uids.remove(client.session)
        
        if len(self._pool) >= CLIENT_POOL_SIZE_MAX:
            now = int(time.time())
            while self._pool:
                k, v = next(iter(self._pool.items()))
                if v.last_access + CLINET_POOL_MAX_AGE < now:
                    self._pool.pop(k)
                else:
                    break

        if len(self._pool) < CLIENT_POOL_SIZE_MAX:
            pool_key = (client.session.sdk.account, type(client.session.sdk).__name__)
            self._pool[pool_key] = ClientCache(client)

    '''
    returns a client from the pool if available, otherwise creates a new one
    client.session.sdk is always set to the provided sdk
    '''
    def get_client(self, sdk: sdkclient) -> PoolClientWrapper:
        pool_key = (sdk.account, type(sdk).__name__)
        if pool_key in self._pool:
            item = self._pool.pop(pool_key)
            # no need to check for last password used, as the client is already logged in, when the session expires, the client will use the new sdk to re-login
            assert item.client.uid not in self.active_uids
            self.active_uids.add(item.client.uid)
            item.client.session.sdk = sdk
            return item.client
        return PoolClientWrapper(sdk)
        

instance = ClientPool()