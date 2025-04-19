from flask import Flask
from routes.user_routes import user_bp
from routes.store_routes import store_bp


def register_routes(app: Flask):
    app.register_blueprint(user_bp, url_prefix=f"/users")
    app.register_blueprint(store_bp, url_prefix=f"/stores")
