import os


class Settings:
    """
    @author: Andriw Rollo,
    @version: v1 2025-04-14
    @functionality: These are the application configuration variables
    """

    HOST = os.getenv("HOST_IP")
    PORT = os.getenv("PORT_HOST")
    DEBUG = os.getenv("DEBUG")

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
