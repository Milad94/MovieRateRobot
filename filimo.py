from decorators import exception_logger
from bs4 import BeautifulSoup


@exception_logger
def parse_page(html_text):
    html_obj = BeautifulSoup(html_text)
