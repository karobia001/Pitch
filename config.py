import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    @staticmethod
    def init_app(app):
        pass
    

class ProdConfig(Config):
    '''
    Production configuration child class
    Args: 
        Config: The parent configuration class with general configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:maich@localhost/pitch'
class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:maich@localhost/pitch'
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class
    Args: 
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
 

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
} 