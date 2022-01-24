import database as _database
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


async def get_product_by_name(name: int, db: _orm.Session):
    return db.query(_models.Product).filter(_models.Product.name == name).first()


async def create_product(product: _schemas.ProductCreate, db: _orm.Session):

    product_obj = _models.Product(
        name=product.name,
        # url=product.url,
        type=product.type,
        pieces=product.pieces,
        in_stock=product.in_stock,
        # date_parsed=product.date_parsed,
    )

    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)
    return product_obj
