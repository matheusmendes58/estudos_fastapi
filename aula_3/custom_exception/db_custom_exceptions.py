
from aula_3.config import settings

class CredentialsErrorConnection(Exception):

    def __init__(self, msg_error: str = 'Erro de conexão com banco de dados verificar credenciais'):
        
        super().__init__(msg_error)

class HostErrorConnection(Exception):

    def __init__(self, msg_error: str = f'Erro de conexão com host "{settings.host_db}"'):

        super().__init__(msg_error)