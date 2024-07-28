from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import entities
import models
import service
import uvicorn
from database import get_db, engine

entities.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def get_health():
    return {
        "status": "Working"
    }


@app.post("/products", response_model=models.Product)
def create_product(product: models.ProductCreate, db: Session = Depends(get_db)):
    return service.create_product(db=db, product=product)


@app.get("/products", response_model=list[models.Product])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_products(db=db, skip=skip, limit=limit)


@app.get("/products/{product_id}", response_model=models.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = service.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.put("/products/{product_id}", response_model=models.Product)
def update_product(product_id: int, product: models.ProductCreate, db: Session = Depends(get_db)):
    db_product = service.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.delete("/products/{product_id}", response_model=models.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = service.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
