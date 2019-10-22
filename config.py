import os

class Config:
    '''
    General configuration class
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:eriko@localhost/mypitches'
    
    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
} 

#  email configurations
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")