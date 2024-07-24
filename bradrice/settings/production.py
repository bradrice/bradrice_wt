# app/app/settings/production.py
from .base import *
import os


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)



print("in production", BASE_DIR)

DJANGO_ROOT = '/home/app/'

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["icons.bradrice.com", "localhost:8009", "0.0.0.0:8009"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://icons.bradrice.com', 'http://0.0.0.0:8009']
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = 'icons.bradrice.com'

print(CSRF_TRUSTED_ORIGINS)


# Database PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),
        'NAME': os.environ.get("DATABASE_NAME"),
        'USER': os.environ.get("DATABASE_USER"),
        'PASSWORD': os.environ.get("DATABASE_PW"),
        'HOST': os.environ.get("SQL_HOST"),
        'PORT': os.environ.get("SQL_PORT"),
    }
}

try:
    from .local import *
except ImportError:
    pass
