import os

class Config:
    '''
    General configuration class
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:eriko@localhost/mypitches'
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
} 