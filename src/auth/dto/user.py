from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    email: str
    name: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = 'user'
    is_active: Optional[bool] = True

    def to_dict(self) -> dict:
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "role": self.role,
            "is_active": self.is_active,
        }

    def validate(self) -> None:
        # TODO : 추가 검증 로직 필요
        errors = []
        if '@' not in self.email:
            errors.append("이메일 형식이 올바르지 않습니다.")
        if len(self.password) < 8:
            errors.append("비밀번호는 최소 8자 이상이어야 합니다.")        
        return (len(errors) == 0, errors)
