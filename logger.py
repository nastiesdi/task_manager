import logging

# logging.basicConfig(filename="sample.log", level=logging.INFO, format='%(funcName)s %(asctime)s - %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

formatter = logging.Formatter('%(funcName)s %(asctime)s - %(message)s')

file_handler = logging.FileHandler('user.log')
file_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)

# def add_info_loger(massage):
#     LOGGER.info(massage)
#     LOGGER.error('Error!!')

