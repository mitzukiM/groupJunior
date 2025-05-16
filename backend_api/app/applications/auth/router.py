from fastapi import APIRouter


router_auth= APIRouter()


@router_auth.post('/login')
async def user_login():
    return
