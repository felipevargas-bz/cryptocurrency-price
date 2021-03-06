import logging


from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings

log = logging.getLogger(__name__)


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.POSTGRES_DATABASE_URL,
        modules={"models": ["app.infra.postgres.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(
        db_url=settings.POSTGRES_DATABASE_URL,
        modules={"models": ["app.infra.postgres.models"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()


# new
if __name__ == "__main__":
    run_async(generate_schema())
