from datetime import datetime
from os import access

from asyncpg.pgproto.pgproto import timedelta

from applications.auth.password_handler import PasswordEncrypt
from applications.users.crud import get_user_by_email
from settings import settings
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
    async def get_login_token_pairs(self, data: OAuth2PasswordRequestForm, session: AsyncSession):
        user_email = data.username
        user_password = data.password
        user = await get_user_by_email(user_email, session)


        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found'
            )

        is_valid_password = await PasswordEncrypt.verify_password(user_password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Incorrect password'
            )

        tokens = await self.generate_token_pairs(user.id)
        return tokens

    async def generate_token_pairs(self, user_id) -> dict:
        payload = {"user_id": user_id}
        access_token = await self.create_token(payload, timedelta(minutes=5))
        refresh_token = await self.create_token(payload, timedelta(days=1))
        return {"access_token": access_token, "refresh_token": refresh_token}


async def create_token(self,payload:dict, expiry:timedelta) -> str:
        now = datetime.now()
        time_payload={"exp" : now + expiry,"iat": now}
        token = jwt.encode(payload | time_payload,self.secret,self.algorithm)
        print(token)
        return token

auth_handler = AuthHandler()


