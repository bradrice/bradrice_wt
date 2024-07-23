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
ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ["localhost", "localhost:8083", "127.0.0.1", "icons.bradrice.com", "[::1]"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['http://localhost:8083', 'http://localhost:8000', 'https://icons.bradrice.com', 'http://icons.bradrice.com']



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
