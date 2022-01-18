from fastapi import APIRouter
from app.api.endpoints import coin


api_router = APIRouter()

api_router.include_router(coin.router, prefix='/coin', tags=['Coin'])
