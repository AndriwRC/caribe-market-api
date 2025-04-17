from http import HTTPStatus
from queries.user_queries import UserQueries
from schemas.requests.user_schema import UserSchema
from utils.objects_model import DataResponse, MessagesUserService


class UserService:
    user_schema = UserSchema()
    user_queries = UserQueries()
    messages = MessagesUserService()

    def get(self, user_id: int = None) -> DataResponse:
        data_response = DataResponse()
        try:
            if not user_id:
                users = self.user_queries.get_all()
                data_response.data = self.user_schema.dump(users, many=True)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.USER_FETCH_SUCCESS
                return data_response

            user = self.user_queries.get_by_id(user_id=user_id)
            if not user:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.USER_NOT_FOUND
                return data_response

            data_response.data = self.user_schema.dump(user)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.USER_FETCH_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.USER_FETCH_ERROR
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            return data_response
