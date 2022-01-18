from typing import Optional
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.schemas.coin import (
    CreateCoin,
    CoinResponse,
    PayloadCoin,
)
from app.services.coin import coin_service


router = APIRouter()


@router.post(
    path='/',
    response_class=JSONResponse,
    response_model=CoinResponse,
    status_code=201,
    responses={201: {"description": "Coin created"}},
)
async def create(coin_in : CreateCoin):
    coin = await coin_service.create_coin(coin=coin_in)
    return coin


@router.get(
    path='/',
    response_class=JSONResponse,
    status_code=201,
    responses={
        201: {"description" : "Coins foud"},
        404: {"description": "Coins not found"}
    }
)
async def get_all(
    *,
    name: str = Query(None),
    skip: int = 0,
    limit: int = 99999,
    ):
    if name is not None:
        coin_in = PayloadCoin(name=name)
    else:
        coin_in = None
    coins = await coin_service.get_all(coin=coin_in, skip=skip, limit=limit)

    return coins
