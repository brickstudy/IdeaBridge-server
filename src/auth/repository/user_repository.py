from src.auth.repository.abc_user_repository import BaseUserRepository
from src.auth.dto.user import User
from supabase import Client
from src.common.exception.exception import DataNotFoundException, DataBaseException
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
                is_active=user["is_active"],
                created_at=user["created_at"],
            )            
        except APIError as e:
            raise DataBaseException(detail=e.message)

    def create_user(self, user_dto: User) -> User:
        pass