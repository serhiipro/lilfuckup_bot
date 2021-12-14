import logging
from datetime import datetime

from data.config import PROJECT_DIRECTORY


def set_handler():
    formatter = logging.Formatter('%(asctime)s %(name)-5s %(levelname)-8s %(message)s')
    filehandler = logging.FileHandler(f'{PROJECT_DIRECTORY}/logs/logger_{datetime.utcnow().strftime("%d_%m_%y")}.log')
    filehandler.setLevel(logging.INFO)
    filehandler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.info('Changing logger')
        logger.handlers.clear()

    logger.addHandler(filehandler)
    logger.info('Logger created')


logging_level = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging_level)
set_handler()
