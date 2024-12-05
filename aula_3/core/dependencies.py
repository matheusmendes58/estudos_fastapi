from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from aula_3.models.database.base_db import DBSESSION

async def get_session() -> Generator:
    session: AsyncSession = DBSESSION

    try:
        yield session
    finally:
        await session.close()
