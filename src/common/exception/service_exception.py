from src.common.exception.exception import AppException
from src.common.exception.exception import ErrorCode

class ServiceException(AppException):
    """Service 관련 예외"""
    pass


class ValidationException(ServiceException):
    """유효성 검증 예외"""
    def __init__(self, error_code: ErrorCode = ErrorCode.VALIDATION_ERROR, message: str = '유효성 검증 실패', detail: str = None):
        super().__init__(error_code, message, detail)
