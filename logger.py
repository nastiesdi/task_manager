import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def add_info_loger(massage):
    logging.info(massage)
    logging.error('Error!!')

