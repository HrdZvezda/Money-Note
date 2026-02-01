import pytest
from app import create_app, db

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@pytest.fixture
def app():
    """建立測試用的flask app"""
    app = create_app(TestConfig)

    yield app # 暫停, 測試開始執行

@pytest.fixture
def client(app):
    """建立測試用的HTTP client"""
    return app.test_client()