# Configuration file for Flask and other settings

class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///agrip.db'  # SQLite database path

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'postgresql://user:password@host/dbname'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
