from typing import List
import fastapi as _fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import sqlalchemy.orm as _orm

import services as _services
import schemas as _schemas

_services.create_database()

app = _fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)


@app.post("/api/product")
async def create_product(
    product: _schemas.ProductIn, db: _orm.Session =
        _fastapi.Depends(_services.get_db),
):
    total_price = product.total_price
    price_url = product.url

    db_product = await _services.get_product_by_name(product.name, db)

    # product already exists, create a new entry in price
    if db_product:
        return await _services.create_price_for_product(
            db_product.id, total_price, price_url, db
        )

    written_product = await _services.create_product(product, db)

    return await _services.create_price_for_product(
        written_product.id, total_price, price_url, db
    )


@app.post("/api/products")
async def create_products(
    products: List[_schemas.ProductIn],
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):

    for product in products:
        total_price = product.total_price
        price_url = product.url

        db_product = await _services.get_product_by_name(product.name, db)

        # product already exists, create a new entry in price
        if db_product:
            await _services.create_price_for_product(
                db_product.id, total_price, price_url, db, True
            )
            continue

        written_product = await _services.create_product(product, db)
        await _services.create_price_for_product(
            written_product.id, total_price, price_url, db, True
        )
        continue

    db.commit()
    # db.refresh()


@app.get("/api/product_prices{product_id}", response_model=List[_schemas.Price])
async def get_product_prices(
    product_id, db: _orm.Session = _fastapi.Depends(_services.get_db),
):

    return await _services.get_prices_per_product(product_id, db=db)


@app.get("/api/products", response_model=List[_schemas.ProductOut])
async def get_products(db: _orm.Session = _fastapi.Depends(_services.get_db),):

    return await _services.get_products(db)


@app.delete("/api/clear_db", response_model=bool)
async def clear_db(db: _orm.Session = _fastapi.Depends(_services.get_db),):

    return await _services.clear_db(db)

