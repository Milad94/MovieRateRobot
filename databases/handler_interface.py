from abc import ABC, abstractmethod


class DatabaseHandler(ABC):
    @abstractmethod
    def insert_movies(self, movies, site):
        pass
