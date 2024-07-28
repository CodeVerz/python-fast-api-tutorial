from sqlalchemy import Column, Integer, String
from database import Base


class ProductEntity(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255))
    quantity = Column(Integer)
