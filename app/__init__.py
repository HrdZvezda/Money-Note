from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class='app.config.Config'):
    """Flask app factory"""
    app = Flask(__name__)

    # load config（支援字串或類別）
    if isinstance(config_class, str):
        app.config.from_object(config_class)
    else:
        app.config.from_object(config_class)

    # init db
    db.init_app(app)

    # 建立資料表
    with app.app_context():
        from app.models import Transaction # 載入model
        db.create_all()


    # register blueprint(avoid circular import)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app