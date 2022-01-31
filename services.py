import database as _database
import datetime as _dt
import models as _models
import sqlalchemy.orm as _orm
import schemas as _schemas


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()

    try:
        yield db
    finally:
        db.close()


async def get_product_by_name(name: str, db: _orm.Session):
    return db.query(_models.Product).filter(_models.Product.name == name).first()


async def create_product(product: _schemas.ProductIn, db: _orm.Session):

    product_obj = _models.Product(
        name=product.name,
        type=product.type,
        total_price=product.total_price,
        pieces=product.pieces,
        in_stock=product.in_stock,
    )

    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)
    return product_obj


async def create_price_for_product(
    product_id: int, total_price: float, price_url: str, db: _orm.Session
):

    price_obj = _models.Price(
        product_id=product_id,
        total_price=total_price,
        price_per_oz=123.32,
        date=_dt.datetime.now(),
        url=price_url,
    )

    db.add(price_obj)
    db.commit()
    db.refresh(price_obj)
    return price_obj


async def get_products(db: _orm.Session):

    return db.query(_models.Product).all()

async def get_prices_per_product(prod_id: int, db: _orm.Session):

    prices = db.query(_models.Price).filter_by(product_id=prod_id)
    return list(map(_schemas.Price.from_orm, prices))
