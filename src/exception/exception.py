from src.exception.error_codes import ErrorCode


class AppException(Exception):
    def __init__(self, error_code: ErrorCode, message: str):
        super().__init__(message)
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.error_code.value}: {self.message}"
    
    def to_dict(self):
        return {
            "error_code": self.error_code.value,
            "message": self.message
        }


class RepositoryException(AppException):
    """Repository 관련 예외"""
    pass


class DataNotFoundException(RepositoryException):
    """데이터를 찾을 수 없는 경우"""
    def __init__(self, message: str = '데이터를 찾을 수 없습니다.'):
        super().__init__(ErrorCode.DATA_NOT_FOUND, message)


class ServiceException(AppException):
    """Service 관련 예외"""
    pass


class ControllerException(AppException):
    """Controller 관련 예외"""
    pass
