import json

from crawlers.interface import Crawler
from decorators import exception_logger
from request import Request


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

    @exception_logger
    def __crawl_pages(self):
        page_number = 100
        while self.crawl:
            urls = [self.page_url.format(i) for i in range(1, page_number)]
            responses = Request.get(urls)
            page_number += 100
            self.__extract_pages(responses)
        return self.pages

    def __extract_pages(self, responses):
        for response in responses:
            if response.ok:
                page = json.loads(response.text)
                if page['result']:
                    self.pages.append(self.__parse_page(page))
                self.crawl = False

    @exception_logger
    def __parse_page(self, page_json):
        data = list()
        for movie in page_json['result']:
            data.append(movie['id'])
        return data

    @exception_logger
    def __crawl_movies(self, pages):
        urls = [self.movie_url.format(movie_id) for movie_id in pages]
        # urls_queue = Queue()
        # for page in pages:
        #     for movie_id in page:
        #         urls_queue.put(self.movie_url.format(movie_id))
        responses = Request.get(urls)
        self.__extract_movie_in_page(responses)

    def __extract_movie_in_page(self, responses):
        for response in responses:
            if response.ok:
                movie_json = json.loads(response.text)
                self.movies_data.append(self.__pars_movie(movie_json))

    @exception_logger
    def __pars_movie(self, movie_json):
        data = dict()
        data['caption'] = movie_json['result']['caption'].replace('\u200c', '')
        data['rate'] = movie_json['result']['hit']
        return data
