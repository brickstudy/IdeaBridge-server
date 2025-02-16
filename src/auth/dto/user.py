from dataclasses import dataclass
from datetime import datetime

from typing import Optional, Type, TypeVar


T = TypeVar("T")


@dataclass
class User:
    email: str
    name: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

    def to_dict(self) -> dict:
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "role": self.role,
            "is_active": self.is_active,
        }