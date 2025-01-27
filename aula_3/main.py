from fastapi import FastAPI

from aula_3.api.v1.api import api_router
from aula_3.config import settings
from custom_exception.db_custom_exceptions import HostErrorConnection, CredentialsErrorConnection
from aula_3.models.database.base_db import create_all

app = FastAPI(title='Cursos API - FastApi SQL Alchemy')
app.include_router(api_router, prefix=settings.api_v1_str)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=8000, log_level='info')
