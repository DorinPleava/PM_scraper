import datetime as _dt
from typing import List, Optional


import pydantic as _pydantic


class Price(_pydantic.BaseModel):
    id: int
    product_id: int
    total_price: float
    price_per_oz: float
    date: _dt.datetime
    url: str

    class Config:
        orm_mode = True


class Product(_pydantic.BaseModel):
    id: int
    name: str
    type: str
    pieces: int
    in_stock: bool


class ProductIn(Product):
    total_price: float
    url: str

    class Config:
        orm_mode = True


class ProductOut(Product):
    prices: List[Price]

    class Config:
        orm_mode = True

