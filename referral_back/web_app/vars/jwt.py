from .rest import *

JWT_ALGORITHM = env.str('JWT_ALGORITHM', 'HS256')

JWT_TOKEN_EXPIRE = env.int('JWT_TOKEN_EXPIRE', 15)
