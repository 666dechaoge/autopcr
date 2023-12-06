from enum import Enum

class eInventoryType(Enum):
    TreasureBox = 0
    Unit = 1
    Item = 2
    EquipEnchant = 3
    Equip = 4
    TeamExp = 5
    Stamina = 6
    RoomItem = 7
    Jewel = 8
    Design = 10
    Piece = 11
    Gold = 12
    ArenaBattleNumber = 13
    GrandArenaBattleNumber = 14
    Emblem = 15
    CustomMypage = 16
    BankGold = 17
    ExtraEquip = 18
    CustomMyPageFrame = 19
    RoomItemLevelUp = 901
    Other = 999
    INVALID_VALUE = -1

class ePromotionLevel(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6
    LEVEL_7 = 7
    LEVEL_8 = 8
    LEVEL_9 = 9
    LEVEL_10 = 10
    LEVEL_11 = 11
    LEVEL_12 = 12
    LEVEL_13 = 13
    LEVEL_14 = 14
    LEVEL_15 = 15
    LEVEL_16 = 16
    LEVEL_17 = 17
    LEVEL_18 = 18
    LEVEL_19 = 19
    LEVEL_20 = 20
    LEVEL_21 = 21
    LEVEL_22 = 22
    LEVEL_23 = 23
    LEVEL_24 = 24
    LEVEL_25 = 25
    LEVEL_26 = 26
    LEVEL_27 = 27
    LEVEL_28 = 28
    LEVEL_29 = 29
    LEVEL_30 = 30
    LEVEL_31 = 31
    LEVEL_32 = 32
    INVALID_VALUE = -1

class ePartyType(Enum):
    QUEST = 1
    ARENA = 2
    ARENA_DEF = 3
    DUNGEON = 4
    GRAND_ARENA_1 = 5
    GRAND_ARENA_2 = 6
    GRAND_ARENA_3 = 7
    GRAND_ARENA_DEF_1 = 8
    GRAND_ARENA_DEF_2 = 9
    GRAND_ARENA_DEF_3 = 10
    STORY = 11
    FAVORITE = 12
    COOP = 13
    CLAN_BATTLE = 14
    HATSUNE = 15
    REPLAY = 16
    TOWER = 17
    TOWER_EX_1 = 18
    TOWER_EX_2 = 19
    TOWER_EX_3 = 20
    SEKAI = 21
    MY_PARTY_EDIT = 22
    RARITY_6_QUEST = 23
    HATSUNE_SPECIAL_BATTLE = 24
    FRIEND_BATTLE = 25
    FRIEND_BATTLE_DEF_1 = 26
    FRIEND_BATTLE_DEF_2 = 27
    FRIEND_BATTLE_DEF_3 = 28
    UEK_TOWER = 31
    SHIORI = 30
    TRIAL_BATTLE = 32
    MY_BATTLE_DEF_1 = 33
    MY_BATTLE_DEF_2 = 34
    MY_BATTLE_DEF_3 = 35
    DIMENSION_FAULT_1 = 36
    DIMENSION_FAULT_2 = 37
    DIMENSION_FAULT_3 = 38
    DIMENSION_FAULT_4 = 39
    DIMENSION_FAULT_5 = 40
    DIMENSION_FAULT_TREASURE = 41
    ROOM_GROUND_FLOOR = 10101
    ROOM_SECOND_FLOOR = 10102
    ROOM_THIRD_FLOOR = 10103
    KAISER_BATTLE_MAIN = 2001
    KAISER_BATTLE_SUB_1 = 1001
    KAISER_BATTLE_SUB_2 = 1002
    KAISER_BATTLE_SUB_3 = 1003
    KAISER_BATTLE_SUB_4 = 1004
    LEGION_BATTLE_MAIN = 2002
    STORY_RAID_EVENT_RAID_1 = 1005
    STORY_RAID_EVENT_RAID_2 = 1006
    STORY_RAID_EVENT_RAID_3 = 1007
    STORY_RAID_EVENT_RAID_4 = 1008
    MIROKU_MAIN_BATTLE = 3008
    INVALID_VALUE = -1

class eClanRole(Enum):
    MEMBER = 0
    SUB_LEADER = 30
    LEADER = 40
    INVALID_VALUE = -1

class eMissionStatusType(Enum):
    NoClear = 0
    EnableReceive = 1
    AlreadyReceive = 2
    ChallengePeriodEnd = 101
    INVALID_VALUE = -1

class eClanChatMessageType(Enum):
    MESSAGE = 0
    STAMP = 1
    DONATION = 2
    JOIN = 3
    LEAVE = 4
    LEADER = 6
    SUB_LEADER = 7
    ORGANIZATION = 8
    REMOVE = 9
    BATTLE_LOG = 10
    FRIEND_BATTLE = 11
    BATTLE_LOG_COMMENT = 12
    FRIEND_BATTLE_COMMENT = 13
    UNREAD = 14
    MINI_GAME_SCORE = 15
    MINI_GAME_TAQ_RECRUITMENT = 16
    INVALID_VALUE = -1

class eClanChatPlayButtonCondition(Enum):
    NONE = 0
    UNOPENED_MINI_GAME_IN_EVENT = 1
    OPENED_MINI_GAME_IN_EVENT = 2
    BEFORE_GAME_TABLE_ADD = 3
    GAME_TABLE_PURCHASED_AFTER_GAME_TABLE_ADD = 4
    GAME_TABLE_UNPURCHASED_AFTER_GAME_TABLE_ADD = 5
    INVALID_VALUE = -1

class eUserClanJoinStatus(Enum):
    NONE = 0
    REQUEST = 1
    JOINING = 2
    SECESSION = 3
    REJECTION = 4
    DELETE = 5
    CANCEL = 6
    EXPULSION = 7
    INVALID_VALUE = -1

class eClanJoinCondition(Enum):
    CONDITION_NONE = 0
    EVERYONE = 1
    ONLY_INVITATION = 2
    DISABLE = 3
    INVALID_VALUE = -1

class eClanActivityGuideline(Enum):
    GUIDELINE_NONE = 0
    GUIDELINE_1 = 1
    GUIDELINE_2 = 2
    GUIDELINE_3 = 3
    GUIDELINE_4 = 4
    GUIDELINE_5 = 5
    GUIDELINE_6 = 6
    GUIDELINE_7 = 7
    GUIDELINE_8 = 8
    GUIDELINE_9 = 9
    GUIDELINE_10 = 10
    GUIDELINE_11 = 11
    GUIDELINE_12 = 12
    GUIDELINE_13 = 13
    GUIDELINE_14 = 14
    GUIDELINE_15 = 15
    GUIDELINE_16 = 16
    GUIDELINE_17 = 17
    INVALID_VALUE = -1

class eGachaType(Enum):
    Gold = 1
    Payment = 2
    FreeOnly = 3
    INVALID_VALUE = -1

class eEventSubStoryStatus(Enum):
    UNREAD = 1
    READED = 2
    ADDED = 3
    PUZZLE_PLACED = 4
    INVALID_VALUE = -1

class eSystemId(Enum):
    ERROR = 0
    NORMAL_QUEST = 101
    HARD_QUEST = 102
    SPECIAL_QUEST = 103
    EXPEDITION_QUEST = 104
    STORY_QUEST = 106
    CLAN_BATTLE = 107
    TOWER = 108
    UNIQUE_EQUIPMENT = 109
    SEKAI = 110
    VERY_HARD = 111
    HIGH_RARITY_EQUIPMENT = 112
    KAISER = 114
    BULK_SKIP = 115
    QUEST_QUADSPEED = 116
    HATSUNE_QUEST_QUADSPEED = 117
    TRAINING_QUEST_QUADSPEED = 118
    EQUIPMENT_QUEST_QUADSPEED = 119
    RARITY_UP_QUEST = 120
    LEGION = 121
    SECRET_DUNGEON = 122
    STORY_RAID_EVENT = 123
    MAIN_QUEST_AUTO = 124
    DIMENSION_FAULT = 125
    NORMAL_SHOP = 201
    ARENA_SHOP = 202
    GRAND_ARENA_SHOP = 203
    EXPEDITION_SHOP = 204
    CLAN_BATTLE_SHOP = 205
    LIMITED_SHOP_OLD = 206
    MEMORY_PIECE_SHOP = 207
    GOLD_SHOP = 208
    JUKEBOX = 209
    COUNTER_STOP_SHOP = 210
    ARCADE = 211
    LIMITED_SHOP = 212
    EX_EQUIPMENT_WEAPON_SHOP = 213
    EX_EQUIPMENT_ARMOR_SHOP = 214
    EX_EQUIPMENT_ACCESSORY_SHOP = 215
    NORMAL_GACHA = 301
    RARE_GACHA = 302
    FESTIVAL_GACHA = 303
    START_DASH_GACHA = 304
    LEGEND_GACHA = 305
    START_PRINCESS_FES_GACHA = 306
    LIMITED_CHARA_GACHA = 307
    RETURN_USER_PRINCESS_FES_GACHA = 308
    UNIT_GROW_UP_GACHA = 309
    NORMAL_ARENA = 401
    GRAND_ARENA = 402
    UNIT_EQUIP = 501
    UNIT_LVUP = 502
    UNIT_SKILL_LVUP = 503
    UNIT_RARITY_UP = 504
    UNIT_STATUS = 505
    UNIT_EQUIP_ENHANCE = 506
    EQUIPMENT_DONATION = 507
    UNIT_GET = 508
    GROWTH_BALL = 509
    REDEEM_UNIT = 510
    EXCEED_LIMIT = 511
    ROOM_1F = 601
    ROOM_2F = 602
    ROOM_3F = 603
    CLAN = 701
    CLAN_MEMBER_LIST = 702
    STORY = 801
    DATA_LINK = 901
    CARTOON = 902
    VOTE = 903
    FRIEND = 904
    FRIEND_BATTLE = 905
    FRIEND_CAMPAIGN = 906
    FRIEND_MANAGEMENT = 907
    CHARA_EXCHANGE_TICKET = 908
    TRIAL_BATTLE = 909
    DAILY_TASK = 910
    TRAVEL = 1001
    HATSUNE_TOP = 6001
    HATSUNE_GACHA = 6002
    HATSUNE_STORY = 6003
    HATSUNE_NORMAL_QUEST = 6004
    HATSUNE_HARD_QUEST = 6005
    HATSUNE_NORMAL_BOSS = 6006
    HATSUNE_HARD_BOSS = 6007
    HATSUNE_COMMON_BOSS = 6008
    HATSUNE_GACHA_TICKET_COLLECTION = 6009
    HATSUNE_VERY_HARD_BOSS = 6010
    HATSUNE_SPECIAL_BOSS = 6011
    HATSUNE_SPECIAL_BOSS_EX = 6012
    UEK_BOSS = 6101
    HATSUNE_REVIVAL_TOP = 7001
    HATSUNE_REVIVAL_GACHA = 7002
    HATSUNE_REVIVAL_STORY = 7003
    HATSUNE_REVIVAL_NORMAL_QUEST = 7004
    HATSUNE_REVIVAL_HARD_QUEST = 7005
    HATSUNE_REVIVAL_NORMAL_BOSS = 7006
    HATSUNE_REVIVAL_HARD_BOSS = 7007
    HATSUNE_REVIVAL_COMMON_BOSS = 7008
    HATSUNE_REVIVAL_GACHA_TICKET_COLLECTION = 7009
    HATSUNE_REVIVAL_VERY_HARD_BOSS = 7010
    HATSUNE_REVIVAL_SPECIAL_BOSS = 7011
    HATSUNE_REVIVAL_SPECIAL_BOSS_EX = 7012
    SHIORI_EVENT_TOP = 8001
    SHIORI_EVENT_STORY = 8003
    SHIORI_EVENT_QUEST_NORMAL = 8004
    SHIORI_EVENT_QUEST_HARD = 8005
    SHIORI_EVENT_NORMAL_BOSS = 8006
    SHIORI_EVENT_HARD_BOSS = 8007
    SHIORI_EVENT_COMMON_BOSS = 8008
    SHIORI_EVENT_VERY_HARD_BOSS = 8010
    INVALID_VALUE = -1

class eShopItemBannerType(Enum):
    NONE = 0
    RED_RIBBON = 1
    BLUE_RIBBON = 2
    GREEN_RIBBON = 3
    INVALID_VALUE = -1

class eExchangeStaminaState(Enum):
    NONE = 0
    ALL_EXCHANGE = 1
    PART_EXCHANGE = 2
    NOT_EXCHANGE = 3
    INVALID_VALUE = -1

class eTaqBuyStatus(Enum):
    NONE = 0
    BUY_TAQ = 1
    BUY_GAMETABLE = 2
    NOT_BUY_GAMETABLE = 3
    NOT_CAN_BUY_GAMETABLE = 4
    INVALID_VALUE = -1

class eBGMKey(Enum):
    HOME = 200
    ROOM_1F = 210
    ROOM_2F = 211
    ROOM_3F = 212
    INVALID_VALUE = -1

class ePkbHappenMode(Enum):
    DRAMATIC = 1
    SIMPLE = 2
    INVALID_VALUE = -1

class eRewardLimitType(Enum):
    NO_LIMIT = 0
    HAS_LIMIT = 1
    INVALID_VALUE = -1

class eStoryStatus(Enum):
    LOCKED = 1
    UNVIEWED = 2
    VIEWING = 3
    INVALID_VALUE = -1

class eSrtCatalogStatus(Enum):
    EnemyUnlock = 1
    EnemyReaded = 2
    PlayerUnlock = 3
    PlayerReaded = 4
    INVALID_VALUE = -1

class eTaqDifficultyLevel(Enum):
    NONE = 0
    NORMAL = 1
    HARD = 2
    VERY_HARD = 3
    INVALID_VALUE = -1

class eTaqQuizType(Enum):
    NONE = 0
    PRICONNE_CONTAIN = 1
    NORMAL = 2
    BOTH = 3
    INVALID_VALUE = -1

class eTaqEntryType(Enum):
    NONE = 0
    ALL = 1
    CLAN_ONLY = 2
    PASSWORD = 3
    RETRY_SAME_MEMBER = 4
    INVALID_VALUE = -1

class eTaqGameServerStatus(Enum):
    NONE = 0
    ROOM = 1
    ANSWER_WAIT = 2
    INTERVAL = 3
    RESULT = 4
    INVALID_VALUE = -1

class eTaqQuizStatus(Enum):
    UNLOCK = 0
    QUESTION_UNREADED = 1
    QUESTION_READED = 2
    ANSWER_UNREADED = 3
    ANSWER_READED = 4
    INVALID_VALUE = -1

class eTravelStartType(Enum):
    NORMAL = 1
    RESTART = 2
    BULK = 3
    ADD_LAP = 8
    RESTART_AND_ADD = 9
    INVALID_VALUE = -1

class eClanSupportMemberType(Enum):
    NONE = 0
    DUNGEON_SUPPORT_UNIT_1 = 1
    DUNGEON_SUPPORT_UNIT_2 = 2
    CLAN_BATTLE_SUPPORT_UNIT_1 = 3
    CLAN_BATTLE_SUPPORT_UNIT_2 = 4

class eGachaDrawType(Enum):
    Free = 1
    Payment = 2
    Ticket = 3
    Discount = 4
    CampaignSingle = 5
    Campaign10Shot = 6
    StartDash = 7
    Legend = 8
    SpecialTicket = 9
    SpFesCmapaign10Shot = 10
    SpFesDiscount10Shot = 11
    INVALID_VALUE = -1

class eSkillLocationCategory(Enum):
    NO_SKILLSLOT = 0
    UNION_BURST_SKILL = 101
    MAIN_SKILL_1 = 201
    MAIN_SKILL_2 = 202
    EX_SKILL_1 = 301
    EX_SKILL_2 = 302
    EX_SKILL_3 = 303
    FREE_SKILL_1 = 401
    FREE_SKILL_2 = 402
    FREE_SKILL_3 = 403
    INVALID_VALUE = -1

