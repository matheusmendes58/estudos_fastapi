from typing import List

from pydantic import ConfigDict

class AllSettings:
    """
    General configs from applications
    """

    def __init__(self):
        # API
        self.api_v1_str = '/api/v1'

        # Mysql
        self.user_db = ''
        self.pwd_db = ''
        self.host_db = ''
        self.db = ''
        self.connect_db = f'mysql+pymysql://{self.user_db}:{self.pwd_db}@{self.host_db}/{self.db}'

settings = AllSettings()