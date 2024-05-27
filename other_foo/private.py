from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from jwt import ExpiredSignatureError
from starlette.requests import Request

secret_key = 'qtioyudsjklafzxcbkjlnvSDFLJKSDLKFJSDf65644231239'
algorithm = 'HS256'


def encode_jwt(payload: dict) -> str:
    expires_delta = timedelta(seconds=600)
    to_encode = payload.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    try:
        token = jwt.encode(
            to_encode,
            key=secret_key,
            algorithm=algorithm
        )
        return token
    except ValueError:
        raise HTTPException(
            status_code=403,
            detail='Invalid private key'
        )


def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, key=secret_key, algorithms=algorithm)
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Expired private key')
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError):
        raise HTTPException(status_code=401, detail='Invalid private key')
    return payload


def get_user_id_by_token(request: Request):
    token = request.cookies.get('token')
    info = decode_jwt(token)
    user_id = info.get('sub')
    return user_id
