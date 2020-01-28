from threading import Thread

import requests

from decorators import exception_logger


class Request:
    @staticmethod
    def get(urls_queue):
        responses = list()
        threads = list()
        for i in range(35):
            t = Thread(target=Request.__send_get_request,
                       args=(urls_queue, responses),
                       daemon=True)
            threads.append(t)
            t.start()
        urls_queue.join()
        for thread in threads:
            thread.join()
        return responses

    @staticmethod
    @exception_logger
    def __send_get_request(urls_queue, responses):
        while not urls_queue.empty():
            responses.append(requests.get(urls_queue.get()))
            urls_queue.task_done()
