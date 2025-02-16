from src.auth.repository.abc_user_repository import BaseUserRepository
from src.auth.dto.user import User
from supabase import Client
from src.common.exception.exception import DataNotFoundException, DataBaseException, DuplicateDataException
from postgrest.exceptions import APIError


class UserRepository(BaseUserRepository):
    def __init__(self, db: Client):
        self.user_table = db.table("users")

    def get_user(self, user_dto: User) -> User:
        try:
            response = self.user_table.select("*").eq("email", user_dto.email).execute()
            if not response.data:
                raise DataNotFoundException
            user =response.data[0]
            return User(
                email=user["email"],
                password=user["password"],
                name=user["name"],
                role=user["role"],
                is_active=user["is_active"]
            )            
        except APIError as e:
            raise DataBaseException(detail=e.message)

    def create_user(self, user_dto: User) -> User:
        try:
            self.user_table.insert(user_dto.to_dict()).execute()
            return user_dto
        except APIError as e:
            if e.code == '23505':
                raise DuplicateDataException(detail=e.message)
            raise DataBaseException(detail=e.message)

    def delete_user(self, user_dto: User) -> None:
        try:
            self.user_table.delete().eq("email", user_dto.email).execute()
        except APIError as e:
            raise DataBaseException(detail=e.message)
