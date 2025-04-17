class DataResponse:

    def __init__(self):
        self.message: str = ""
        self.errors: dict | list = {}
        self.data: dict | list = {}
        self.status: int = 200


class MessagesUserService:
    USER_NOT_FOUND = "User not found."
    USER_FETCH_SUCCESS = "User data retrieved successfully."
    USER_FETCH_ERROR = "An error occurred while retrieving user data."

    USER_CREATED_SUCCESS = "User created successfully."
    USER_CREATION_ERROR = "An error occurred while creating the user."
    USER_EMAIL_EXISTS = "The user email already exists."

    USER_UPDATED_SUCCESS = "User updated successfully."
    USER_UPDATE_ERROR = "An error occurred while updating the user."

    USER_DELETED_SUCCESS = "User deleted successfully."
    USER_DELETE_ERROR = "An error occurred while deleting the user."
