import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database.base_models import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    uuid_data: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4)



    title: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(10000), index=True, default="")
    price: Mapped[float] = mapped_column(nullable = False)
    main_image:Mapped[str] = mapped_column(nullable=False)
    images:Mapped[list[str]] = mapped_column(ARRAY(String), default=list)


    def __str__(self):
        return f'Product {self.title} - {self.id}'

class Cart(Base):
    __tablename__ = "carts"


class CartProduct(Base):
    __tablename__ = "cart_products"


    cart_id : Mapped[int] = mapped_column(ForeignKey("carts.id"))
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id"))
    price: Mapped[float] = mapped_column(default=0.0)
    quantity: Mapped[float] = mapped_column(default=0.0)
