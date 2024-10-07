from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_app_db',
        'USER': 'test_user',
        'PASSWORD': 'SecurePass123',
        'HOST': '168.232.167.90',
        'PORT': '5432',
    }
}