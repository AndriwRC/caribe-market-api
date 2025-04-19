from flask import Blueprint
from views.phone_views import PhoneAPI

phone_bp = Blueprint("phone", __name__)

phone_views = PhoneAPI.as_view("phone_api")
phone_bp.add_url_rule("/", view_func=phone_views, methods=["GET"])
phone_bp.add_url_rule("/<int:phone_id>", view_func=phone_views, methods=["GET"])
