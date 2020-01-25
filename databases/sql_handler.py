from databases.factory import database_factory
from databases.handler_interface import DatabaseHandler
from decorators import exception_logger

from models.sql import Movie, Filimo, Namava, FilmNet


class SQLDatabaseHandler(DatabaseHandler):
    @exception_logger
    def __init__(self):
        self.db = database_factory()
        self.db.connect()
        self.db.create_tables(
            [Movie, Filimo, Namava,
             FilmNet])

    @exception_logger
    def __save_movie(self, movie):
        movie_instance = Movie.create(caption=movie['caption'])
        movie_instance.save()
        return movie_instance

    @exception_logger
    def __insert_if_not_exist(self, movie, site):
        movie_instance = self.__save_movie(movie)
        return eval(site).create(rate=movie['rate'],
                                 movie=movie_instance)

    @exception_logger
    def __insert_if_exist(self, movie, site):
        return eval(site).create(rate=movie['rate'],
                                 movie=self.get_movie_from_db_if_exist(
                                     movie))

    @exception_logger
    def insert_movies(self, movies, site):
        for movie in movies:
            instance = self.save_movie_in_db(
                self.get_movie_from_db_if_exist(movie))
            instance(movie, site).save()

    @exception_logger
    def get_movie_from_db_if_exist(self, movie):
        try:
            record = Movie.get(Movie.caption == movie['caption'])
        except:
            return False
        return record

    @exception_logger
    def save_movie_in_db(self, is_exist):
        if bool(is_exist):
            return self.__insert_if_exist
        return self.__insert_if_not_exist
