class DataResponse:

    def __init__(self):
        self.message: str = ""
        self.errors: dict | list = {}
        self.data: dict | list = {}
        self.status: int = 200


class MessagesService:
    def __init__(self, entity: str):
        self.entity = entity.capitalize()

        self.NOT_FOUND = f"{self.entity} not found."
        self.FETCH_SUCCESS = f"{self.entity} data retrieved successfully."
        self.FETCH_ERROR = (
            f"An error occurred while retrieving {self.entity.lower()} data."
        )

        self.CREATED_SUCCESS = f"{self.entity} created successfully."
        self.CREATION_ERROR = (
            f"An error occurred while creating the {self.entity.lower()}."
        )
        self.DUPLICATE = f"The {self.entity.lower()} already exists."

        self.UPDATED_SUCCESS = f"{self.entity} updated successfully."
        self.UPDATE_ERROR = (
            f"An error occurred while updating the {self.entity.lower()}."
        )

        self.DELETED_SUCCESS = f"{self.entity} deleted successfully."
        self.DELETE_ERROR = (
            f"An error occurred while deleting the {self.entity.lower()}."
        )
