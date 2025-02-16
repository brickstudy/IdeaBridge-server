from src.common.exception.error_codes import ErrorCode


class AppException(Exception):
    def __init__(self, error_code: ErrorCode, message: str, detail: str = None):
        super().__init__(message)
        self.error_code = error_code
        self.message = message
        self.detail = detail

    def __str__(self):
        return f"{self.error_code.value}: {self.message}"
    
    def to_dict(self):
        return {
            "error_code": self.error_code.value,
            "message": self.message,
            "detail": self.detail
        }


class RepositoryException(AppException):
    """Repository 관련 예외"""
    pass


class DataNotFoundException(RepositoryException):
    """데이터를 찾을 수 없는 경우"""
    def __init__(self, error_code: ErrorCode = ErrorCode.DATA_NOT_FOUND, message: str = '데이터를 찾을 수 없습니다.', detail: str = None):
        super().__init__(error_code, message, detail)


class DataBaseException(RepositoryException):
    """데이터베이스 예외"""
    def __init__(self, error_code: ErrorCode = ErrorCode.DATABASE_ERROR, message: str = '데이터베이스 오류', detail: str = None):
        super().__init__(error_code, message, detail)

class ServiceException(AppException):
    """Service 관련 예외"""
    pass


class ControllerException(AppException):
    """Controller 관련 예외"""
    pass
