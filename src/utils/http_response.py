from flask import jsonify
from utils.objects_model import DataResponse


def http_response(response: DataResponse | dict):
    if isinstance(response, DataResponse):
        return (
            jsonify(
                {
                    "message": response.message,
                    "data": response.data,
                    "errors": response.errors,
                    "status": response.status,
                }
            ),
            response.status,
        )

    return jsonify(response), response.get("status", 500)
