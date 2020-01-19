from request import send_get_request
from parse_filimo import parse_page
from parse_namava import parse_page
from parse_filmnet import parse_page
from decorators import exception_logger


@exception_logger
def crawl_filimo():
    pass


@exception_logger
def crawl_namava(url):
    pass


@exception_logger
def crawl_filmnet(url):
    pass
