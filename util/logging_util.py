import logging


class Logging:
    def __init__(self, level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)


def init_logger():
    logger = Logging().logger

    file_handler = logging.FileHandler(
        filename="../logs/etl.log",
        mode="a",
        encoding="UTF-8"
    )

    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
    )

    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger
