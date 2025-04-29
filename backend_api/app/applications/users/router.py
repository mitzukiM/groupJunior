from fastapi import APIRouter,status
from applications.users.schemas import BaseFields, RegisterUserField, BaseFields

router_users = APIRouter()

@router_users.post("/create",status_code=status.HTTP_201_CREATED)
async def create_user(
        new_user:RegisterUserField
) -> BaseFields:
    return new_user