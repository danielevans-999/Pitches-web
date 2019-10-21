class Config:
    '''
    General configuration class
    '''
    
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