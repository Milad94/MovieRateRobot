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
    page_number = 1
    pages = list()
    while crawl:
        response = send_get_request(url.format(page_number))
        page_number += 1
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
        for movie_id in page:
            response = send_get_request(movie_url.format(movie_id))
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
