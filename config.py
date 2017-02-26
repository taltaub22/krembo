import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '$2b$31$i60/2S/Mdf0050zqJjljae'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    DEBUG = False
