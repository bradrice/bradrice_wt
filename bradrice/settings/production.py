# app/app/settings/production.py
from .base import *

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

print(env)

DJANGO_ROOT = '/home/app/'

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

# Database PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': env("SQL_ENGINE"),
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PW"),
        'HOST': env("SQL_HOST"),
        'PORT': env("SQL_PORT"),
    }
}

try:
    from .local import *
except ImportError:
    pass
