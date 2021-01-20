from .common import *
import os
import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get_value('DB_NAME', cast=str, default=''),
        'USER': env('DB_USER', cast=str, default=''),
        'PASSWORD': env('DB_PASSWORD', cast=str, default=''),
        'PORT': env('DB_PORT', cast=int, default=None),
        'HOST': env('DB_HOST', cast=str, default=''),
    }
}

SECRET_KEY = env.get_value('SECRET_KEY', default='secret')
