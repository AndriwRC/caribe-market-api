from flask import request
from flask.views import MethodView
from utils.http_response import http_response
from services.user_service import UserService


class UserAPI(MethodView):
    service = UserService()

    def get(self, user_id=None):
        response_data = self.service.get(user_id=user_id)
        return http_response(response_data)

    def post(self, user_id=None):
        response_data = self.service.create(data=request.get_json())
        return http_response(response_data)

    def put(self, user_id: int):
        response_data = self.service.update(user_id=user_id, data=request.get_json())
        return http_response(response_data)

    def delete(self, user_id: int):
        response_data = self.service.delete(user_id=user_id)
        return http_response(response_data)
