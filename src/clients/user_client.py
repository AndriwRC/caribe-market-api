import requests


class UserServiceClient:
    BASE_URL = "http://localhost:8080/users"

    @staticmethod
    def get_user(user_id: int):
        try:
            response = requests.get(f"{UserServiceClient.BASE_URL}/{user_id}")
            response.raise_for_status()
            return response.json().get("data")
        except requests.RequestException as ex:
            return None
