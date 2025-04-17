from config.settings import Settings


class Connection:
    URI = f"postgresql+psycopg2://{Settings.DB_USER}:{Settings.DB_PASSWORD}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"
    TRACK_MODIFICATIONS = True
