import json

from crawlers.interface import Crawler
from decorators import exception_logger
from request import send_parallel_requests


class NamavaCrawler(Crawler):

    def __init__(self):
        self.movies_data = list()
        self.movie_url = "https://www.namava.ir/api/v1.0/medias/{}/preview"
        self.page_url = "https://www.namava.ir/api/v1.0/medias/latest-movies?pi={}&ps=30"
        self.crawl = True
        self.pages = list()

    def get_data(self):
        self.__crawl()
        return self.movies_data

    @exception_logger
    def __crawl(self):
        self.pages = self.__crawl_pages()
        self.__crawl_movies(self.pages)

    def __create_movies_url_list(self, page):
        movie_urls = list()
        for movie_id in page:
            movie_urls.append(self.movie_url.format(movie_id))
        return movie_urls

    def __extract_movie_in_page(self, responses):
        for response in responses:
            if response.ok:
                movie_json = json.loads(response.text)
                self.movies_data.append(self.__pars_movie(movie_json))

    @exception_logger
    def __crawl_movies(self, pages):
        for page in pages:
            movie_urls = self.__create_movies_url_list(page)
            responses = send_parallel_requests(movie_urls)
            self.__extract_movie_in_page(responses)

    def __check_last_page(self, page):
        if not page['result']:
            self.crawl = False
        return self.crawl

    def __extract_pages(self, responses):
        for response in responses:
            if response.ok:
                page = json.loads(response.text)
                if self.__check_last_page(page):
                    self.pages.append(self.__parse_page(page))

    @exception_logger
    def __crawl_pages(self):
        page_number = 100
        while self.crawl:
            urls = [self.page_url.format(i) for i in range(1, page_number)]
            responses = send_parallel_requests(urls)
            page_number += 100
            self.__extract_pages(responses)
        return self.pages

    @exception_logger
    def __parse_page(self, page_json):
        data = list()
        for movie in page_json['result']:
            data.append(movie['id'])
        return data

    @exception_logger
    def __pars_movie(self, movie_json):
        data = dict()
        data['caption'] = movie_json['result']['caption'].replace('\u200c', '')
        data['rate'] = movie_json['result']['hit']
        return data
