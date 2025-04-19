from http import HTTPStatus
from marshmallow import ValidationError
from queries.user_queries import UserQueries
from schemas.requests.user_schema import UserSchema
from utils.objects_model import DataResponse, MessagesService


class UserMessagesService(MessagesService):
    def __init__(self, entity):
        super().__init__(entity)
        self.USER_EMAIL_EXISTS = "The user email already exists."


class UserService:
    user_schema = UserSchema()
    user_queries = UserQueries()
    messages = UserMessagesService("user")

    def get(self, user_id: int = None) -> DataResponse:
        data_response = DataResponse()
        try:
            if not user_id:
                users = self.user_queries.get_all()
                data_response.data = self.user_schema.dump(users, many=True)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.FETCH_SUCCESS
                return data_response

            user = self.user_queries.get_by_id(user_id=user_id)
            if not user:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            data_response.data = self.user_schema.dump(user)
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
            user_data = self.user_schema.load(data)
            if self.user_queries.email_exists(user_data.email):
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.CREATION_ERROR
                data_response.errors = [
                    {"email": [self.messages.USER_EMAIL_EXISTS, user_data.email]}
                ]
                return data_response

            new_user = self.user_queries.create_user(user_data)
            data_response.data = self.user_schema.dump(new_user)
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

    def update(self, user_id: int, data: dict):
        data_response = DataResponse()
        try:
            user = self.user_queries.get_by_id(user_id=user_id)
            if not user:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            self.user_schema.load(data=data, partial=True)

            self.user_queries.update_user(user_id=user_id, data=data)
            data_response.data = self.user_schema.dump(user)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.UPDATED_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.UPDATE_ERROR
            if isinstance(ex, ValidationError):
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.errors = ex.args
                return data_response

            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = ex.args
            return data_response

    def delete(self, user_id: int):
        data_response = DataResponse()
        try:
            user = self.user_queries.get_by_id(user_id=user_id)
            if not user:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            deleted_user = self.user_queries.delete_user(user=user)
            data_response.data = self.user_schema.dump(deleted_user)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.DELETED_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.DELETE_ERROR
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = ex.args
            return data_response
