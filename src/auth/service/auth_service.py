from src.auth.repository.user_repository import UserRepository
from src.auth.dto.user import User
from src.auth.dto.request import UserCreateRequest
from src.common.exception.service_exception import ValidationException
from supabase import Client


class AuthService:
    def __init__(self, client: Client):
        self.user_repository = UserRepository(client)

    def register_user(self, request: UserCreateRequest) -> User:
        # Check Validation
        user_dto = request.to_dto()
        is_valid, errors = user_dto.validate()
        if not is_valid:
            raise ValidationException(message="email, 비밀번호가 올바르지 않습니다. : " + ", ".join(errors))
        
        # Check Duplicate
        user = self.user_repository.get_user_with_email(user_dto.email)
        if user:
            raise ValidationException(message="이미 존재하는 이메일입니다.")

        # Create User
        return self.user_repository.create_user(user_dto)
