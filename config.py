import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE_URL = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DATABASE_URL = os.environ.get('DATABASE_URL')
