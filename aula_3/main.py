#TODO Criar tabelas e realiar testes no banco de dados
from traceback import TracebackException

from custom_exception.db_custom_exceptions import HostErrorConnection, CredentialsErrorConnection
from aula_3.models.database.base_db import create_all

if __name__ == '__main__':
    try:
        create_all()

    except Exception:
        raise HostErrorConnection

    except Exception:
        raise CredentialsErrorConnection
