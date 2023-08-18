from .swg import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': env.str('DEV_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': env.str('DEV_DB_NAME', 'db_name'),
        'USER': env.str('DEV_DB_USER', 'user'),
        'PASSWORD': env.str('DEV_DB_PASSWORD', 'password'),
        'HOST': env.str('DEV_DB_HOST', '127.0.0.1'),
        'PORT': env.int('DEV_DB_PORT', 5432),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CORS_ALLOWED_ORIGINS = ['http://localhost:8080']
