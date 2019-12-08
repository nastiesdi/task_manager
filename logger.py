import logging


def _get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.ERROR)
    file_handler = logging.FileHandler('user.log')
    formatter = logging.Formatter('%(funcName)s %(levelname)s %(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
