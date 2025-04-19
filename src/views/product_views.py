from flask import request
from flask.views import MethodView
from utils.http_response import http_response
from services.product_service import ProductService


class ProductAPI(MethodView):
    service = ProductService()

    def get(self, product_id=None):
        response_data = self.service.get(product_id=product_id)
        return http_response(response_data)

    def post(self, product_id=None):
        response_data = self.service.create(data=request.get_json())
        return http_response(response_data)

    # def put(self, product_id: int):
    #     response_data = self.service.update(product_id=product_id, data=request.get_json())
    #     return http_response(response_data)

    # def delete(self, product_id: int):
    #     response_data = self.service.delete(product_id=product_id)
    #     return http_response(response_data)
