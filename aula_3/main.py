
from fastapi import FastAPI
from fastapi.openapi.models import Example

from sqlalchemy.exc import OperationalError, ArgumentError

from aula_3.api.v1.api import api_router
from aula_3.config import settings
from custom_exception.db_custom_exceptions import StringConnection, CredentialsErrorConnection
from aula_3.models.database.base_db import create_all

app = FastAPI(title='Cursos API - FastApi SQL Alchemy')
app.include_router(api_router, prefix=settings.api_v1_str)

if __name__ == '__main__':
    import uvicorn

    try:
        create_all()

    except OperationalError:
        raise CredentialsErrorConnection()

    except ArgumentError:
        raise StringConnection()

    except Exception as e:
        raise 'Erro Desconhecido'

    uvicorn.run('main:app', port=8000, log_level='info')
