from datetime import datetime
from os import name
from typing import Any, Dict, List, Union

from tortoise.query_utils import Prefetch

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.coin import Coin
from app.schemas.coin import CreateCoin, UpdateCoin

PAYLOAD_DATA = {
    "name": "message__name",
    "is_coin": "message__is_coin",
    "is_read": "message__is_read",
    "is_deleted": "message__is_deleted",
}


class CRUDCoin(CRUDBase[Coin, CreateCoin, UpdateCoin]):
    def __get_right_keys(self, *, payload):
        payload = {
            (PAYLOAD_DATA.get(k) if k in PAYLOAD_DATA else k): v
            for (k, v) in payload.items()
        }
        return payload

    async def create(self, *, obj_in: CreateCoin) -> Union[dict, None]:
        coin_data = obj_in.dict()
        coin = await self.model.create(message_id=obj_in.message_, **coin_data)
        return coin

    async def get_by_name(self, *, name: str) -> Union[dict, None]:
        model = (
            await self.model.filter(name=name)
            .prefetch_related("message__name")
            .all()
        )
        if model:
            return model[0]
        return None

    async def get_all(
        self,
        *,
        payload: dict = None,
        name: str,
        skip: int = 0,
        limit: int = 10,
    ) -> List:
        if payload:
            payload = self.__get_right_keys(payload=payload)
            model = (
                await self.model.filter(
                    name=name, **payload
                )
                .offset(skip)
                .limit(limit)
                .all()
                .prefetch_related(
                    "name",
                )
            )
        else:
            model = (
                await self.model.filter(message__name=name)
                .all()
                .offset(skip)
                .limit(limit)
                .prefetch_related(
                    "name",
                )
            )
        return model

    async def update(self, *, id: int, obj_in: Dict[str, Any]) -> bool:
        obj_in = self.__get_right_keys(payload=obj_in)
        model = await self.model.get(id=id)
        await model.update_from_dict(obj_in).save()
        return True


coin = CRUDCoin(Coin)
