import logging
import inspect

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(name)s : %(asctime)s : %(levelname)s : %(message)s')
        logger.addHandler(filehandler)
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)

        return logger
