import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '!@#456&*(agcGbjE#B^d!@brs^'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    DEBUG = False
