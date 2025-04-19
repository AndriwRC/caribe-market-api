from http import HTTPStatus
from marshmallow import ValidationError
from queries.store_queries import StoreQueries
from schemas.requests.store_schema import StoreSchema
from utils.objects_model import DataResponse, MessagesService
from clients.user_client import UserServiceClient


class StoreMessagesService(MessagesService):
    def __init__(self, entity):
        super().__init__(entity)
        self.USER_NOT_FOUND = "The user with the giving owner_id doesn't exists."


class StoreService:
    store_schema = StoreSchema()
    store_queries = StoreQueries()
    messages = StoreMessagesService("store")

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

    def create(self, data: dict):
        data_response = DataResponse()
        try:
            store_data = self.store_schema.load(data)
            if not UserServiceClient.get_user(store_data.owner_id):
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.CREATION_ERROR
                data_response.errors = [{"owner_id": [self.messages.USER_NOT_FOUND]}]
                return data_response

            new_store = self.store_queries.create_store(store_data)
            data_response.data = self.store_schema.dump(new_store)
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATED_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.CREATION_ERROR
            if isinstance(ex, ValidationError):
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.errors = ex.args
                return data_response

            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            return data_response
