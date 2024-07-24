# app/app/settings/production.py
from .base import *
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))


print("in production")

DJANGO_ROOT = '/home/app/'

SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["icons.bradrice.com", "localhost:8009", "0.0.0.0:8009"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://icons.bradrice.com', 'http://0.0.0.0:8009']
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = 'icons.bradrice.com'

print(ALLOWED_HOSTS)


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
