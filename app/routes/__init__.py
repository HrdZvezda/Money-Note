from flask import Blueprint

# 建立主要bp
main_bp = Blueprint('main', __name__)

# 載入路由(這會執行 main.py 裡的 @main_bp.route)
from app.routes import main # 首頁
from app.routes import transaction # 交易 