from flask import request
from flask.views import MethodView
from utils.http_response import http_response
from services.store_service import StoreService


class StoreAPI(MethodView):
    service = StoreService()

    def get(self, store_id=None):
        response_data = self.service.get(store_id=store_id)
        return http_response(response_data)

    def post(self):
        response_data = self.service.create(data=request.get_json())
        return http_response(response_data)

    # def put(self, store_id: int):
    #     response_data = self.service.update(store_id=store_id, data=request.get_json())
    #     return http_response(response_data)

    # def delete(self, store_id: int):
    #     response_data = self.service.delete(store_id=store_id)
    #     return http_response(response_data)
