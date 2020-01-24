from database import DatabaseHandler
from factory import crawler_factory


class Facade:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.filimo_crawler = crawler_factory("FILIMO")
        self.namva_crawler = crawler_factory("NAMAVA")
        self.filmnet_crawler = crawler_factory("FILIMNET")

    def run(self):
        # filimo_data = self.filimo_crawler.get_data()
        # self.db_handler.insert_movies(filimo_data, "Filimo")
        namva_data = self.namva_crawler.get_data()
        self.db_handler.insert_movies(namva_data, "Namava")
        # filmnet_data = self.filmnet_crawler.get_data()
        # self.db_handler.insert_movies(filmnet_data, "FilmNet")
