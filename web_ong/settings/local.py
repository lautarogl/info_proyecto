from .base import *

SECRET_KEY = 'django-insecure-99806r&-=*0i7*q@-5e22=0of3pzz%kue0!*q7d)9zd@ut^#je'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'***',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0',
        }
    },
}"""