from math import factorial
from queue import Queue
from threading import Thread
from loguru import logger
from func_time import func_time

THREADS_COUNT = 10
q = Queue()


def worker():
    while 1:
        item = q.get()
        res = factorial(item)
        factorial_length = str(res)
        # q2.put(factorial_length)
        logger.info('Processed {}. Length is {}', item, factorial_length)
        q.task_done()


@func_time
def wait_queue(qu):
    qu.join()


if __name__ == '__main__':
    logger.info('Starting main')

    for _ in range(THREADS_COUNT):
        thread = Thread(
                target=worker,
                daemon=True,
            )
        thread.start()

    logger.info('Fulfilling queue')
    for calc_item in range(9500,9900):
        q.put(calc_item)
    logger.info('Waiting..')
    wait_queue(q)
    logger.info('Finished main')
