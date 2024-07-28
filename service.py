from sqlalchemy.orm import Session
from entities import ProductEntity
from models import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = ProductEntity(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProductEntity).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(ProductEntity).filter(ProductEntity.id == product_id).first()


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(ProductEntity).filter(ProductEntity.id == product_id).first()

    if db_product is None:
        return None

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductEntity).filter(ProductEntity.id == product_id).first()

    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()
    return db_product
