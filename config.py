import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '4E\xdfIm\x08\xbc*i\xf2\x8b\xd6\xb7\xbb\x1b\x90\x84\xe0\x91\xa7\xdf\xfc\xfd\x9f'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False