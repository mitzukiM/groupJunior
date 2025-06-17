from fastapi import APIRouter

products_router = APIRouter()

@products_router.post('/')
async def create_product():
    return


@products_router.get('/{pk}')
async def get_product(pk: int):
    return

@products_router.get('/')
async def get_products():
    return