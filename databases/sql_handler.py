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
    def insert_movies(self, movies, site):
        for movie in movies:
            movie_record = self.select_movie(movie)
            if movie_record:
                instance = eval(site).create(rate=movie['rate'],
                                             movie=self.select_movie(
                                                 movie))
            else:
                movie_instance = self.__insert_movie_caption(movie)
                movie_instance.save()
                instance = eval(site).create(rate=movie['rate'],
                                             movie=movie_instance)
            instance.save()

    @exception_logger
    def __insert_movie_caption(self, movie):
        movie_instance = Movie.create(caption=movie['caption'])
        movie_instance.save()
        return movie_instance

    @exception_logger
    def select_movie(self, movie):
        try:
            record = Movie.get(Movie.caption == movie['caption'])
        except:
            return False
        return record
