
from aula_3.config import settings

class CredentialsErrorConnection(Exception):

    def __init__(self, msg_error: str = f'Erro de conexão com banco de dados verificar credenciais'
                                        f' de usuario senha e database'):
        
        super().__init__(msg_error)

class HostErrorConnection(Exception):

    def __init__(self, msg_error: str = f'Erro de conexão com host "{settings.host_db}"'):

        super().__init__(msg_error)

class StringConnection(Exception):
    def __init__(self, msg_error: str = 'Erro na string de conexão com banco de dados'
                                        'Exemplo: myysql+pymysql://root:xxxx@localhost/estudo_api_fastapi '
                                        '- mysql escrito de maneira errada'):

        super().__init__(msg_error)

class InvalidField(Exception):

    def __init__(self, msg_error: str = 'Violação de integridade no banco de dados (campo duplicado ou inválido).'):

        super().__init__(msg_error)
