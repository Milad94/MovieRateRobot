from crawlers.factory import crawler_factory
from databases.factory import handler_factory


class Facade:
    def __init__(self):
        self.db_handler = handler_factory()
        self.filimo_crawler = crawler_factory("FILIMO")
        self.namva_crawler = crawler_factory("NAMAVA")
        self.filmnet_crawler = crawler_factory("FILIMNET")

    def run(self):
        # filimo_data = self.filimo_crawler.get_data()
        # self.db_handler.insert_movies(filimo_data, "Filimo")
        namava_data = self.namva_crawler.get_data()
        self.db_handler.insert_movies(namava_data, "Namava")
        # filmnet_data = self.filmnet_crawler.get_data()
        # self.db_handler.insert_movies(filmnet_data, "FilmNet")
