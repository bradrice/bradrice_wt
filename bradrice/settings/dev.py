from .base import *
import os
from dotenv import load_dotenv

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

load_dotenv()

DEBUG = True

SECRET_KEY = str(os.getenv('SECRET_KEY'))

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": str(os.getenv('DATABASE_NAME')),
        "USER": str(os.getenv('DATABASE_USER')),
        "PASSWORD": str(os.getenv('DATABASE_PW')),
        "HOST": "db",
        "PORT": "5432",
    }
}


try:
    from .local import *
except ImportError:
    pass
