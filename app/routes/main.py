from app.routes import main_bp

@main_bp.route('/')
def index():
    """Homepage"""
    return {'message': '智能財務管家啟動成功！'}


@main_bp.route('/health')
def health():
    """Health check - check server normally run"""
    return {'status': 'ok'}
