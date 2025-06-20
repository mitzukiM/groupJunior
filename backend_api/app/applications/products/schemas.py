from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    price: float
    main_image: str
    images: list[str]


