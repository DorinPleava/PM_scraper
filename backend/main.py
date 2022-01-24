import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas

app = _fastapi.FastAPI()


@app.post("/api/products")
async def create_product(
    product: _schemas.ProductCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    db_product = await _services.get_product_by_name(product.name, db)

    if db_product:
        raise _fastapi.HTTPException(status_code=400, detail="Product already preset")

    return await _services.create_product(product, db)
