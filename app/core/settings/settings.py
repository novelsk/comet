import os
from ..database.backend import DatabaseArgs

DATABASE = {
    'DRIVER': 'postgres',
    'NAME': os.environ.get('POSTGRES_DB'),
    'USER': os.environ.get('POSTGRES_USER'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    'HOST': 'db',
    'PORT': '5432',
}

TORTOISE_ORM = {
    "connections": {"default": DatabaseArgs(DATABASE).get_url()},
    "apps": {
        "models": {
            "models": ["web.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


class LazySettings:
    DATABASE = None
    TORTOISE_ORM = None

    def __init__(self, settings_dict=None):
        if settings_dict is not None:
            self.__dict__.update(settings_dict)
