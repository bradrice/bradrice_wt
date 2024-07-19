from .base import *

DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
