import uuid

from applications.database.base_models import  Base
from sqlalchemy.orm import Mapper,mapped_column
from sqlalchemy import String
from datetime import datetime
from sqlalchemy.sql import func
import uuid

class User(Base):
    __tablename__='users'

    id:Mapper[int]=mapped_column(primary_key=True)
    created_at:Mapper[datetime] = mapped_column(default=func.now())
    update_at:Mapper[datetime] = mapped_column(default=func.now(),onupdate=func.now())
    uuid_data:Mapper[datetime] = mapped_column(default=uuid.uuid4)


    name:Mapper[str] = mapped_column(String(100),index=True,nullable=False)
    email:Mapper[str]=mapped_column(unique=True,nullable=False)
    hashed_password:Mapper[str]=mapped_column(nullable=False)

