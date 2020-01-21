import grequests
import requests

from decorators import exception_logger


@exception_logger
def send_get_request(url):
    return requests.get(url)


@exception_logger
def send_parallel_requests(urls):
    rs = (grequests.get(u) for u in urls)
    return grequests.map(rs)
