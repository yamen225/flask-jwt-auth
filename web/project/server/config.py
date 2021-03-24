# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_user_name = os.getenv('DATABASE_USER', 'database_user')
database_password = os.getenv('DATABASE_PASSWORD', 'database_password')
database_host = os.getenv('SQL_HOST', 'host')
database_port = os.getenv('SQL_PORT', '')
# postgres_local_base = 'postgresql://sohba_user:password@localhost/'
postgres_local_base = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/'.format(
    database_user_name, database_password, database_host, database_port
)
database_name = os.getenv('DATABASE_NAME', 'my_schema')


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
