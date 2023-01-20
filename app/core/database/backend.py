class DatabaseArgs:
    NAME = 'tortoise'
    PORT = '5432'
    HOST = 'db'
    PASSWORD = ''
    USER = 'root'
    DRIVER = 'postgres'

    def __init__(self, db_dict=None):
        if db_dict is not None:
            self.__dict__.update(db_dict)

    def get_url(self):
        return f'{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}'
