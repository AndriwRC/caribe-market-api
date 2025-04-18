from flask import Blueprint
from views.user_views import UserAPI

user_bp = Blueprint("user", __name__)

user_views = UserAPI.as_view("user_api")
user_bp.add_url_rule(
    "/", view_func=user_views, methods=["GET", "POST"], defaults={"user_id": None}
)
user_bp.add_url_rule("/<int:user_id>", view_func=user_views, methods=["GET", "PUT"])
