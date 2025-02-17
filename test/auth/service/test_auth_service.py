import time
import pytest
from src.auth.service.auth_service import AuthService
from src.auth.repository.user_repository import UserRepository
from src.auth.dto.user import User
from src.auth.dto.request import UserCreateRequest
from src.common.exception.service_exception import ValidationException


class TestAuthService:
    EMAIL = "service@test.com"
    PASSWORD = "test12341234"
    NAME = "test"
    
    @pytest.fixture
    def user_repository(self, client):
        return UserRepository(client)
    
    @pytest.fixture
    def auth_service(self, client):
        return AuthService(client)
    
    @pytest.fixture(autouse=True)
    def setup_and_cleanup(self, user_repository):
        yield
        user_repository.delete_user(User(email=self.EMAIL))
    
    def test_can_register_user(self, auth_service, user_repository):
        # given
        request = UserCreateRequest(email=self.EMAIL, password=self.PASSWORD, name=self.NAME)
        
        # when
        result = auth_service.register_user(request)
        
        # then
        assert result.email == self.EMAIL
        assert result.password == self.PASSWORD
        assert result.name == self.NAME
        
        # time.sleep(1)
        
        ori_user = user_repository.get_user_with_email(self.EMAIL)
        assert ori_user is not None
        assert ori_user.email == self.EMAIL
        assert ori_user.password == self.PASSWORD
        assert ori_user.name == self.NAME
        
        # given
        request = UserCreateRequest(email=self.EMAIL, password=self.PASSWORD, name=self.NAME)
        
        # when
        with pytest.raises(ValidationException):
            auth_service.register_user(request)
    
    def test_can_not_register_user_with_invalid_email(self, auth_service):
        # given
        request = UserCreateRequest(email="invalid_email", password=self.PASSWORD, name=self.NAME)
        
        # when
        with pytest.raises(ValidationException):
            auth_service.register_user(request)
    
    def test_can_not_register_user_with_short_password(self, auth_service):
        # given
        request = UserCreateRequest(email=self.EMAIL, password="short", name=self.NAME)
        
        # when
        with pytest.raises(ValidationException):
            auth_service.register_user(request)
    
    def test_login(self):
        pass
