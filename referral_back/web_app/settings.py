import os
import environ

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SETTINGS_DIR = os.path.join(BASE_DIR, 'web_app')

env = environ.Env()
env.read_env(os.path.join(SETTINGS_DIR, '.env'))

"""
    В зависимости от значения START в файле .env
    выбираем нужную конфигурацию проекта
"""

if env.str('START', 'DEV') == 'PROD':
    print('Server running in production\n')
    from .vars.prod import *
else:
    print('Server running in development\n')
    from .vars.dev import *
