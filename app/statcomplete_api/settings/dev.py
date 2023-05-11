from .base import *

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS += [
    'reset_migrations',
]

SIMPLE_JWT.update(REFRESH_TOKEN_LIFETIME= timedelta(days=15))