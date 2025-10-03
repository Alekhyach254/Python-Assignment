import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    LOG_PROFILE = 'dev'
    # DEV-specific configuration

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    LOG_PROFILE = 'prod'
    # PROD-specific configuration

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(env_name):
    return config.get(env_name, config['default'])