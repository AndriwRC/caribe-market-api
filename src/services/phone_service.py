from http import HTTPStatus
from marshmallow import ValidationError
from queries.phone_queries import PhoneQueries
from schemas.requests.phone_schema import PhoneSchema
from utils.objects_model import DataResponse, MessagesService


class PhoneService:
    phone_schema = PhoneSchema()
    phone_queries = PhoneQueries()
    messages = MessagesService("phone")

    def get(self, phone_id: int = None) -> DataResponse:
        data_response = DataResponse()
        try:
            if not phone_id:
                phones = self.phone_queries.get_all()
                data_response.data = self.phone_schema.dump(phones, many=True)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.FETCH_SUCCESS
                return data_response

            phone = self.phone_queries.get_by_id(phone_id=phone_id)
            if not phone:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_FOUND
                return data_response

            data_response.data = self.phone_schema.dump(phone)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.FETCH_SUCCESS
            return data_response

        except Exception as ex:
            data_response.message = self.messages.FETCH_ERROR
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            return data_response
