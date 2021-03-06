from web.auth.blueprints.register import auth_register_bp
from web.auth.blueprints.login import auth_login_bp
from web.auth.blueprints.avatar import auth_avatar_bp
from web.auth.blueprints.home import auth_home_bp


def auth_register_blueprints(app):
    app.register_blueprint(auth_register_bp)
    app.register_blueprint(auth_login_bp)
    app.register_blueprint(auth_avatar_bp)
    app.register_blueprint(auth_home_bp)
