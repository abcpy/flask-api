from app.app import Flask

"""
注册蓝图到falsk核心对象
"""
def register_blueprints(app):
    from app.api.v1 import create_blueprint
    app.register_blueprint(create_blueprint(),url_prefix='/v1')

def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    register_plugin(app)
    return app