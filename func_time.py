from loguru import logger
from time import time


def func_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        logger.info('it took {:3f} seconds', end - start)
    return wrapper
