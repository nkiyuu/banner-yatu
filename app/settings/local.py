from .common import *
import os
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

SECRET_KEY = env.get_value('SECRET_KEY', default='secret')
