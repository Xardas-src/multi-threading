from loguru import logger as logger
from time import sleep, time
# import logging
from multiprocessing.pool import ThreadPool
import requests
import threading

# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger(__name__)


def process_google_results(query: str) -> int:
    logger.info('Started searching for {!r}', query)
    response = requests.get(
        'https://www.google.com/search',
        params={'q': query},
        # timeout=(5, 10),
    )
    text = response.text
    # result = parse_search_results_for_query(query, text)
    # save_result_to_db(result)
    sleep(1)
    response_len = len(text)
    logger.info('Finished processing query {!r} with result len {}', query, response_len)
    return response_len


if __name__ == '__main__':
    logger.info('Starting main')


    # queries = (
    #     'iphone',
    #     'samsung',
    #     'huawei',
    # )
    #
    # threads = []
    # for query in queries:
    #     thread = threading.Thread(
    #         target=process_google_results,
    #         args=(query, ),
    #     )
    #     thread.start()
    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.join()

    queries = (
        'iphone',
        'samsung',
        'huawei',
        'xiaomi',
        'pycharm',
        'jetbrains',
        'vscode',
        'yandex',
        'goole',
    )
    start = time()
    pool = ThreadPool(len(queries))
    results = pool.map(process_google_results, queries)
    end = time()
    logger.info('it took {:3f} seconds', end - start)
    logger.info('results: {}', results)

    logger.info('Finished main')
