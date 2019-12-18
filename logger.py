import logging


def _get_logger(log_file_name):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file_name)
    formatter = logging.Formatter('%(funcName)s %(levelname)s %(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
