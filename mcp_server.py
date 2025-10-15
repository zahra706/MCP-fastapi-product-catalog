from fastmcp import FastMCP
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product as ProductModel

mcp = FastMCP(name="Product Catalog MCP Server")

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@mcp.tool()
def list_products() -> List[dict]:
    db = next(get_db_session())
    products = db.query(ProductModel).all()
    return [dict(id=p.id, name=p.name, price=p.price, description=p.description) for p in products]

@mcp.tool()
def get_product(product_id: int) -> dict:
    db = next(get_db_session())
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product:
        return dict(id=product.id, name=product.name, price=product.price, description=product.description)
    return {"error": "Product not found"}

if __name__ == "__main__":
    mcp.run()
