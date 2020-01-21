import time

import grequests

from request import send_get_request
from decorators import exception_logger
import filimo
import namava
import filmnet
import json


@exception_logger
def _crawl_namva_pages():
    url = "https://www.namava.ir/api/v1.0/medias/latest-movies?pi={}&ps=30"
    crawl = True
    page_number = 100
    pages = list()
    while crawl:
        urls = [url.format(i) for i in range(1, page_number)]
        rs = (grequests.get(u) for u in urls)
        responses = grequests.map(rs)
        page_number += 100
        for response in responses:
            if response.ok:
                page = json.loads(response.text)
                if page['result']:
                    pages.append(namava.parse_page(page))
                else:
                    crawl = False
    return pages


@exception_logger
def _crawl_namava_movies(pages):
    movies_data = list()
    movie_url = "https://www.namava.ir/api/v1.0/medias/{}/preview"
    for page in pages:
        movie_urls = list()
        for movie_id in page:
            movie_urls.append(movie_url.format(movie_id))
        rs = (grequests.get(u) for u in movie_urls)
        responses = grequests.map(rs)
        for response in responses:
            if response.ok:
                movie_json = json.loads(response.text)
                movies_data.append(namava.pars_movie(movie_json))
    return movies_data


@exception_logger
def crawl_filimo():
    pass


@exception_logger
def crawl_namava():
    pages = _crawl_namva_pages()
    return _crawl_namava_movies(pages)


@exception_logger
def crawl_filmnet(url):
    pass
