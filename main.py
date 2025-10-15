from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Product as ProductModel

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Catalog API", description="A simple API for managing a product catalog")

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

@app.get("/")
def home():
    return {"message": "Welcome to the Product Catalog API!"}

@app.get("/products", response_model=List[Product])
def list_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
