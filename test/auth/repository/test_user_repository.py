import pytest
from src.auth.repository.user_repository import UserRepository
from src.auth.dto.user import User


class TestUserRepository:
    
    @pytest.fixture
    def user_repository(self, client):
        return UserRepository(client)
    
    def test_get_user(self, user_repository):
        # given
        email = "test@test.com"
        
        # when
        user = user_repository.get_user(User(email=email))
        
        # then
        print(user)
        assert user is not None
