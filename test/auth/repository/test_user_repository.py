import pytest
from src.auth.repository.user_repository import UserRepository
from src.auth.dto.user import User
from src.common.exception.exception import DuplicateDataException, DataNotFoundException

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
        assert user.email == email
        
    def test_can_create_user(self, user_repository):
        # given
        email = "kim1@test.com"
        name = "test"
        password = "test"
        role = "user"
        is_active = True
        
        # when
        user = user_repository.create_user(User(email=email, name=name, password=password, role=role, is_active=is_active))
        
        # then
        assert user is not None
        
    def test_can_not_create_user_with_duplicate_email(self, user_repository):
        # given
        email = "kim1@test.com"
        name = "test"
        password = "test"
        role = "user"
        is_active = True
        
        # when
        with pytest.raises(DuplicateDataException):
            user_repository.create_user(User(email=email, name=name, password=password, role=role, is_active=is_active))

    def test_can_delete_user(self, user_repository):
        # given
        email = "kim1@test.com"
        
        # when
        user_repository.delete_user(User(email=email))
        
        # then
        with pytest.raises(DataNotFoundException):
            user_repository.get_user(User(email=email))
