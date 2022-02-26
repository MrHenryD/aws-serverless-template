# Standard library imports
import os


class AppConfig:
    NAME: str = "app"


class LoggerConfig:
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
    LOG_FORMAT = os.environ.get(
        "LOG_LEVEL",
        "%(asctime)s %(levelname)s %(message)s %(module)s %(lineno)d %(funcName)s",
    )
