import os

class Config:
    '''
    General configuration class
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:eriko@localhost/mypitches'
    
    
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:eriko@localhost/mypitches'
    
    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
    # 'test':TestConfig
} 

