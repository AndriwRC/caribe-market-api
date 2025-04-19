from http import HTTPStatus
from marshmallow import ValidationError
from queries.store_queries import StoreQueries
from schemas.requests.store_schema import StoreSchema
from utils.objects_model import DataResponse, MessagesService


class StoreService:
    store_schema = StoreSchema()
    store_queries = StoreQueries()
    messages = MessagesService("store")

    def get(self, store_id: int = None) -> DataResponse:
        data_response = DataResponse()
        try:
            if not store_id:
                stores = self.store_queries.get_all()
                data_response.data = self.store_schema.dump(stores, many=True)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.FETCH_SUCCESS
                return data_response

            store = self.store_queries.get_by_id(store_id=store_id)
            if not store:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            data_response.data = self.store_schema.dump(store)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.FETCH_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.FETCH_ERROR
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            return data_response
