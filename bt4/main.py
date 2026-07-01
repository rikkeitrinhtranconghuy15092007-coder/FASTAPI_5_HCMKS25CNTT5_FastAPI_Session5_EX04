from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field

app = FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]

class ProductUpdate(BaseModel):
    code: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)


@app.get("/products")
def get_products():
    return products


@app.put("/products/{product_id}")
def update_product(
    product_in: ProductUpdate,
    product_id: int = Path(...)
):
    target_product = None
    for item in products:
        if item["id"] == product_id:
            target_product = item
            break
            
    if target_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
        
    for item in products:
        if item["code"] == product_in.code and item["id"] != product_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product code already exists"
            )
            
    target_product["code"] = product_in.code
    target_product["name"] = product_in.name
    target_product["price"] = product_in.price
    target_product["stock"] = product_in.stock
    
    return {
        "message": "Cập nhật sản phẩm thành công",
        "product": target_product
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)