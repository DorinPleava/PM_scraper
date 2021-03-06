import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database


class Product(_database.Base):
    __tablename__ = "products"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    type = _sql.Column(_sql.String)
    total_price = _sql.Column(_sql.Float)
    pieces = _sql.Column(_sql.Integer)
    in_stock = _sql.Column(_sql.Boolean, unique=False, default=False)

    prices = _orm.relationship("Price", back_populates="price")


class Price(_database.Base):
    __tablename__ = "prices"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    product_id = _sql.Column(_sql.Integer, _sql.ForeignKey("products.id"))
    total_price = _sql.Column(_sql.Float)
    price_per_oz = _sql.Column(_sql.Float)
    date = _sql.Column(_sql.DateTime, default=_dt.datetime.now())
    url = _sql.Column(_sql.String)

    price = _orm.relationship("Product", back_populates="prices")
