from flask import request
from flask.views import MethodView
from utils.http_response import http_response
from services.phone_service import PhoneService


class PhoneAPI(MethodView):
    service = PhoneService()

    def get(self, phone_id=None):
        response_data = self.service.get(phone_id=phone_id)
        return http_response(response_data)

    def post(self, phone_id=None):
        response_data = self.service.create(data=request.get_json())
        return http_response(response_data)

    # def put(self, phone_id: int):
    #     response_data = self.service.update(phone_id=phone_id, data=request.get_json())
    #     return http_response(response_data)

    # def delete(self, phone_id: int):
    #     response_data = self.service.delete(phone_id=phone_id)
    #     return http_response(response_data)
