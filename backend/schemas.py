import datetime as _dt

import pydantic as _pydantic

class _ProductBase(_pydantic.BaseModel):
    url: str

class ProductCreate(_pydantic.BaseModel):
    name: str
    type: str
    url: str
    total_price: float
    pieces: int
    in_stock: bool

    class Config:
        orm_mode = True

class Product(_ProductBase):
    id: int
    name: str
    url: str
    type: str
    pieces: int
    in_stock: bool
    date_parsed: _dt.datetime 

    class Config:
        orm_mode = True

class _PriceBase(_pydantic.BaseModel):
    total_price: float
    price_per_oz: float

class PriceCreate(_PriceBase):
    pass

class Price(_PriceBase):
    id: int
    product_id: int
    total_price: float
    price_per_oz: float
    date: _dt.datetime

    class Config:
        orm_mode = True