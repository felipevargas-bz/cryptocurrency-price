from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseCoin(BaseModel):
    name : Optional[str]
    E : Optional[datetime]
    t : Optional[str]
    T : Optional[str]
    s : Optional[str]
    i : Optional[str]
    f : Optional[str]
    L : Optional[str]
    o : Optional[str]
    c : Optional[str]
    h : Optional[str]
    l : Optional[str]
    v : Optional[str]
    n : Optional[str]
    x : Optional[str]
    q : Optional[str]
    V : Optional[str]
    Q : Optional[str]
    B : Optional[str]


class CreateCoin(BaseCoin):
    pass


class PayloadCoin(BaseModel):
    pass


class UpdateCoin(BaseModel):
    pass


class CoinInDB(BaseModel):
    id: int
    name : Optional[str]
    E : Optional[str]
    t : Optional[str]
    T : Optional[str]
    s : Optional[str]
    i : Optional[str]
    f : Optional[str]
    L : Optional[str]
    o : Optional[str]
    c : Optional[str]
    h : Optional[str]
    l : Optional[str]
    v : Optional[str]
    n : Optional[str]
    x : Optional[str]
    q : Optional[str]
    V : Optional[str]
    Q : Optional[str]
    B : Optional[str]

    class Config:
        orm_mode = True


class CoinResponse(BaseModel):
    name : Optional[str]
    E : Optional[str]
    t : Optional[str]
    T : Optional[str]
    s : Optional[str]
    i : Optional[str]
    f : Optional[str]
    L : Optional[str]
    o : Optional[str]
    c : Optional[str]
    h : Optional[str]
    l : Optional[str]
    v : Optional[str]
    n : Optional[str]
    x : Optional[str]
    q : Optional[str]
    V : Optional[str]
    Q : Optional[str]
    B : Optional[str]

    class Config:
        orm_mode = True
