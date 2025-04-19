from flask import Blueprint
from views.product_views import ProductAPI

product_bp = Blueprint("product", __name__)

product_views = ProductAPI.as_view("product_api")
product_bp.add_url_rule("/", view_func=product_views, methods=["GET"])
product_bp.add_url_rule("/<int:product_id>", view_func=product_views, methods=["GET"])
