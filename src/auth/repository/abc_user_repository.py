from abc import ABC, abstractmethod

from src.auth.dto.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    def get_user_with_email(self, email: str) -> User:
        pass

    @abstractmethod
    def create_user(self, user_dto: User) -> User:
        pass
    
    @abstractmethod
    def delete_user(self, user_dto: User) -> None:
        pass
