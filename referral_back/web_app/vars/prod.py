from .swg import *

DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', [])

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': env.str('DB_NAME', 'db_name'),
        'USER': env.str('DB_USER', 'user'),
        'PASSWORD': env.str('DB_PASSWORD', 'password'),
        'HOST': env.str('DB_HOST', '127.0.0.1'),
        'PORT': env.int('DB_PORT', 5432),
    }
}

MEDIA_ROOT = f'\\\\{env.str("PROD_MEDIA_ROOT", os.path.join(BASE_DIR, "media"))}'

STATIC_ROOT = f'\\\\{env.str("PROD_STATIC_ROOT", os.path.join(BASE_DIR, "static"))}'
