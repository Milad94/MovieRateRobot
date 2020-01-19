import requests

from decorators import exception_logger


@exception_logger
def send_get_request(url):
    return requests.get(url)
