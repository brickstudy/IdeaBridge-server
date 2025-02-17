from src.common.exception.error_codes import ErrorCode
from src.common.exception.exception import AppException


class UtilException(AppException):
    """Util 관련 예외"""
    pass


class TokenException(UtilException):
    """토큰 관련 예외"""
    def __init__(self, error_code: ErrorCode = ErrorCode.TOKEN_ERROR, message: str = '토큰 오류', detail: str = None):
        super().__init__(error_code, message, detail)
