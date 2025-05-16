from fastapi import APIRouter ,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from database.session_dependencies import get_async_session
from applications.auth.auth_handler import auth_handler
router_auth= APIRouter()


@router_auth.post('/login')
async def user_login(
        data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_async_session),
):
    token_pair = await auth_handler.get_login_token_pairs(data, session)
    return token_pair
