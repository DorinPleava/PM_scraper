import datetime as _dt


import pydantic as _pydantic


class Product(_pydantic.BaseModel):
    id: int
    name: str
    url: str
    type: str
    total_price: float
    pieces: int
    in_stock: bool
    date_parsed: _dt.datetime

    class Config:
        orm_mode = True


class Price(_pydantic.BaseModel):
    id: int
    product_id: int
    total_price: float
    price_per_oz: float
    date: _dt.datetime

    class Config:
        orm_mode = True


class ProductOut(_pydantic.BaseModel):
    id: int
    name: str
    url: str
    type: str
    prices: list[Price]
    pieces: int
    in_stock: bool
    date_parsed: _dt.datetime

    class Config:
        orm_mode = True
