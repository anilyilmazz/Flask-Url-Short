import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    RESTX_MASK_SWAGGER = False

class AppConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/url'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/url'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@testdb:5432/url'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    app=AppConfig,
    local=LocalConfig,
    test=TestConfig
)
