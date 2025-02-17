from pydantic import BaseModel
from src.auth.dto.user import User


class UserCreateRequest(BaseModel):
    email: str
    password: str
    name: str
    
    def to_dto(self) -> User:
        return User(
            email=self.email,
            password=self.password,
            name=self.name
        )

