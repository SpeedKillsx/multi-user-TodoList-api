import time
from typing import Dict, Optional
import jwt
from decouple import config
from jwt import ExpiredSignatureError, InvalidTokenError

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str) -> Dict[str, str]:
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "exp": time.time() + 600 
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_jwt(token: str) -> Optional[dict]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except ExpiredSignatureError:
        print("Token expiré")
        return None
    except InvalidTokenError:
        print("Token invalide")
        return None
