import logging
import sys

from pythonjsonlogger import jsonlogger  # type: ignore

from settings import LoggerConfig  # type: ignore


def _get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Stream Handler
    sysHandler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(LoggerConfig.LOG_FORMAT)
    sysHandler.setFormatter(formatter)

    logger.addHandler(sysHandler)
    logger.setLevel(LoggerConfig.LOG_LEVEL)
    return logger
