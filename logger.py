import logging

# logging.basicConfig(filename="sample.log", level=logging.INFO, format='%(funcName)s %(asctime)s - %(message)s')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
TASK_LOG = logging.getLogger(__name__).getChild('tasks')
TASK_LOG.setLevel(logging.INFO)

formatter = logging.Formatter('%(funcName)s %(levelname)s %(asctime)s - %(message)s')

file_handler = logging.FileHandler('user.log')
file_handler.setFormatter(formatter)
task_file_handler = logging.FileHandler('tasks.log')
task_file_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)
TASK_LOG.addHandler(task_file_handler)



