from .base import *
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('DATABASE_NAME'),
        "USER": env('DATABASE_USER'),
        "PASSWORD": env('DATABASE_PW'),
        "HOST": "db",
        "PORT": "5432",
    }
}


try:
    from .local import *
except ImportError:
    pass
