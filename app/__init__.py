from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Flask app factory"""
    app = Flask(__name__)

    # load config
    app.config.from_object('app.config.Config')

    # init db
    db.init_app(app)

    # register blueprint(avoid circular import)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app