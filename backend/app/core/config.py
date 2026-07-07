import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "RSOD Agent Platform")

    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

    DEBUG = os.getenv("DEBUG", "true").lower() == "true"


settings = Settings()
