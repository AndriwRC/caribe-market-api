from flask import Flask
from routes.user_routes import user_bp
from routes.store_routes import store_bp
from routes.product_routes import product_bp
from routes.phone_routes import phone_bp


def register_routes(app: Flask):
    app.register_blueprint(user_bp, url_prefix=f"/users")
    app.register_blueprint(store_bp, url_prefix=f"/stores")
    app.register_blueprint(product_bp, url_prefix=f"/products")
    app.register_blueprint(phone_bp, url_prefix=f"/phones")
