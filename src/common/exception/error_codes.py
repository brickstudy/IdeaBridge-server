from enum import Enum


class ErrorCode(Enum):    
    # 10000 ~ 19999: 시스템 관련 오류
    SYSTEM_ERROR = 10000
    
    # 20000 ~ 29999: Repository 관련 오류
    DATABASE_ERROR = 20000
    DATA_NOT_FOUND = 20001
    DUPLICATE_DATA = 20002

    # 30000 ~ 39999: Service 관련 오류
    
    # 40000 ~ 49999: Controller 관련 오류
    
    # 50000 ~ 59999: Util 관련 오류
    TOKEN_ERROR = 50000
