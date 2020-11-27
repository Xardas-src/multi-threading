import math
import multiprocessing
from loguru import logger
from func_time import func_time

# SHARED MEMORY!
from multiprocessing import shared_memory


@func_time
def calc_factorials(factor_args):
    # factorials = list(map(math.factorial, factorials_args))
    # factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    # print(factorials_lengths)

    pool = multiprocessing.Pool(processes=4)
    factorials = pool.map(math.factorial, factor_args)
    factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    print(factorials_lengths)


if __name__ == '__main__':
    logger.info('Starting main')
    factorials_args = range(9500, 9900)
    calc_factorials(factorials_args)
    logger.info('Finished main')