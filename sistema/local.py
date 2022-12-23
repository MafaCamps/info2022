from .settings import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'paginablogbd',
        "USER": 'root123',
        "PASSWORD": 'root123',
        "HOST": 'localhost',
        "PORT": '3306',
    }
}