from .base import *

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.authen.auth.authenticate.AuthBackend',
        'rest_framework.authentication.TokenAuthentication',
    ]
}