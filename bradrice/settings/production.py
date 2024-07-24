# app/app/settings/production.py
from .base import *
import os
from dotenv import load_dotenv



PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

load_dotenv()

print("in production", BASE_DIR)

DJANGO_ROOT = '/home/app/'

SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALLOWED_HOSTS = ["icons.bradrice.com", "localhost:8009", "0.0.0.0:8009"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://.bradrice.com' ]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = 'icons.bradrice.com'

print(CSRF_TRUSTED_ORIGINS)


# Database PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': str(os.getenv("SQL_ENGINE")),
        'NAME': str(os.getenv("DATABASE_NAME")),
        'USER': str(os.getenv("DATABASE_USER")),
        'PASSWORD': str(os.getenv("DATABASE_PW")),
        'HOST': str(os.getenv("SQL_HOST")),
        'PORT': str(os.getenv("SQL_PORT")),
    }
}

try:
    from .local import *
except ImportError:
    pass
