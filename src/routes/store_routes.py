from flask import Blueprint
from views.store_views import StoreAPI

store_bp = Blueprint("store", __name__)

store_views = StoreAPI.as_view("store_api")
store_bp.add_url_rule(
    "/", view_func=store_views, methods=["GET", "POST"], defaults={"store_id": None}
)
store_bp.add_url_rule("/<int:store_id>", view_func=store_views, methods=["GET"])
