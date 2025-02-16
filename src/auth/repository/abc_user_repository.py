from abc import ABC, abstractmethod

from src.auth.dto.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_dto: User) -> User:
        pass

    @abstractmethod
    def create_user(self, user_dto: User) -> User:
        User
    
    
