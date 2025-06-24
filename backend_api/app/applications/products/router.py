from typing import Annotated
from applications.products.crud import create_product_in_db, get_products_data
from fastapi import APIRouter, Body, UploadFile, Depends
import uuid
from applications.products.schemas import ProductSchema,SearchParamsSchema
from applications.products.crud import create_product_in_db
from services.s3.s3 import s3_storage
from sqlalchemy.ext.asyncio import AsyncSession
from applications.users.models import User
from applications.auth.security import get_current_user,admin_required
from applications.users.crud import create_user_in_db, get_user_by_email, activate_user_account
from applications.users.schemas import BaseUserInfo, RegisterUserFields
from database.session_dependencies import get_async_session

products_router = APIRouter()


@products_router.post('/', dependencies=[Depends(admin_required)])
async def create_product(
        main_image: UploadFile,
        images: list[UploadFile] = None,
        title: str = Body(max_length=100),
        description: str = Body(max_length=1000),
        price: float = Body(gt=1),
        session: AsyncSession = Depends(get_async_session),
) -> ProductSchema:
    product_uuid = uuid.uuid4()
    product_uuid_str = str(product_uuid)
    main_image = await s3_storage.upload_product_image(main_image, product_uuid=product_uuid)
    images = images or []
    images_urls = []
    for image in images:
        url = await s3_storage.upload_product_image(image, product_uuid=product_uuid)
        images_urls.append(url)
    created_product = await  (
        create_product_in_db(product_uuid=product_uuid, title=title, description=description, price=price,
                                main_image=main_image, images=images_urls, session=session))
    return created_product
@products_router.get('/{pk}')
async def get_product(pk: int):
    return
@products_router.get('/')
async def get_products(params: Annotated[SearchParamsSchema, Depends()], session: AsyncSession = Depends(get_async_session)):
    result = await get_products_data(params, session)
    return result