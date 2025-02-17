import jwt
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional

from src.common.config import Config
from src.common.exception.util_exception import TokenException

class TokenManager:
    def __init__(self):
        config = Config.get_jwt()
        self.SECRET_KEY = config["secret_key"]
        self.ALGORITHM = config["algorithm"]

    def generate_access_token(self, user_id: str) -> str:
        """
        Access 토큰 생성
        유효기간: 1시간
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(hours=1),
            'iat': datetime.now(timezone.utc),
            'token_type': 'access'
        }
        access_token = jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm=self.ALGORITHM
        )
        return access_token

    def generate_refresh_token(self, user_id: str) -> str:
        """
        Refresh 토큰 생성
        유효기간: 14일
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.now(timezone.utc) + timedelta(days=14),
            'iat': datetime.now(timezone.utc),
            'token_type': 'refresh'
        }
        
        refresh_token = jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm=self.ALGORITHM
        )
        return refresh_token
    
    def generate_tokens(self, user_id: str) -> Dict[str, str]:
        """
        Access 토큰과 Refresh 토큰을 동시에 생성
        """
        access_token = self.generate_access_token(user_id)
        refresh_token = self.generate_refresh_token(user_id)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def verify_token(self, token: str, token_type: Optional[str] = None) -> Dict:
        """
        토큰 검증 및 디코드
        """
        try:
            payload = jwt.decode(
                token,
                self.SECRET_KEY,
                algorithms=[self.ALGORITHM]
            )
            
            # 토큰 타입 검증
            if token_type and payload['token_type'] != token_type:
                raise TokenException(message=f"토큰 타입이 일치하지 않습니다. type: {token_type}")    
            return payload
        except jwt.ExpiredSignatureError:
            raise TokenException(message="토큰이 만료되었습니다.")
        except jwt.InvalidTokenError:
            raise TokenException(message="유효하지 않은 토큰입니다.")

    def refresh_access_token(self, refresh_token: str) -> Dict[str, str]:
        """
        refresh 토큰을 사용하여 새로운 access 토큰 발급
        """
        try:
            # refresh 토큰 검증
            payload = self.verify_token(refresh_token, token_type='refresh')
            
            # 새로운 access 토큰 발급
            user_id = payload['user_id']
            new_access_token = self.generate_access_token(user_id)
            return {
                'access_token': new_access_token,
                'refresh_token': refresh_token
            }
        except Exception as e:
            raise TokenException(message=f"토큰 갱신 실패", detail=str(e))


if __name__ == "__main__":
    token_manager = TokenManager()
    
    user_id = 'testuser@test.com'
    tokens = token_manager.generate_tokens(user_id)

    print("Initial Access Token:", tokens['access_token'])
    print("Initial Refresh Token:", tokens['refresh_token'])
    
    try:
        print("\nSimulating expired access token...")
        expired_access_token = "expired_token"
        token_manager.verify_token(expired_access_token, token_type='access')
    except Exception as e:
        print("Access token verification failed:", str(e))
        
        try:
            print("\nTrying to refresh access token...")
            new_tokens = token_manager.refresh_access_token(tokens['refresh_token'])
            print("New Access Token:", new_tokens['access_token'])

            payload = token_manager.verify_token(new_tokens['access_token'])
            print("New token payload:", payload)
            
        except Exception as refresh_error:
            print("Failed to refresh token:", str(refresh_error))