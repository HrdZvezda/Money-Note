import os

class Config:
    """Base configuration"""
    # Secret Key
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

    # PostgreSQL DB連線
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://money_note:password@db:5432/money_note_db'    
    )

    # Trun off SQLAlchemy 事件追蹤(省效能)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False

# Setting 
config = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}