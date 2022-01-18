from typing import List, TypeVar, Union

from app.crud.base import ICrudBase
from app.infra.postgres.crud.coin import coin
from app.schemas.coin import CreateCoin, PayloadCoin, UpdateCoin

QueryType = TypeVar("QueryType", bound=ICrudBase)


class CoinService:
    def __init__(self, coin_queries: QueryType):
        self.__coin_queries = coin_queries

    async def create_coin(self, coin: CreateCoin) -> Union[dict, None]:
        new_coin_id = await self.__coin_queries.create(obj_in=coin)
        return new_coin_id

    async def get_coin_by_name(self, coin_name: str) -> Union[dict, None]:
        coin = await self.__coin_queries.get_by_id(name=coin_name)
        if coin:
            return coin
        return None

    async def get_all(
        self, *, coin: PayloadCoin, skip: int, limit: int
    ) -> List:
        if coin:
            coin_data = coin.dict(exclude_none=True)
        else:
            coin_data = None
        coins = await self.__coin_queries.get_all(
            payload=coin_data, skip=skip, limit=limit
        )
        return coins

    async def update_coin(self, coin_id: int, new_coin: UpdateCoin) -> bool:
        new_coin_data = new_coin.dict()
        payload = {
            key: value
            for (key, value) in new_coin_data.items()
            if (value not in [None, ""] and key not in ["coin_status_", "message"])
        }
        current_update = await self.__coin_queries.update(id=coin_id, obj_in=payload)
        return current_update

    async def remove_coin(self, coin_id: int) -> int:
        coin_removed_id = await self.__coin_queries.delete(id=coin_id)
        return coin_removed_id


coin_service = CoinService(coin_queries=coin)
