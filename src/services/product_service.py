from http import HTTPStatus
from marshmallow import ValidationError
from queries.product_queries import ProductQueries
from schemas.requests.product_schema import ProductSchema
from utils.objects_model import DataResponse, MessagesService


class ProductService:
    product_schema = ProductSchema()
    product_queries = ProductQueries()
    messages = MessagesService("product")

    def get(self, product_id: int = None) -> DataResponse:
        data_response = DataResponse()
        try:
            if not product_id:
                products = self.product_queries.get_all()
                data_response.data = self.product_schema.dump(products, many=True)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.FETCH_SUCCESS
                return data_response

            product = self.product_queries.get_by_id(product_id=product_id)
            if not product:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            data_response.data = self.product_schema.dump(product)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.FETCH_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.FETCH_ERROR
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            return data_response
