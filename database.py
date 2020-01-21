from config import db
from decorators import exception_logger
from models.filimo import Filimo
from models.filmnet import FilmNet
from models.movie import Movie
from models.namava import Namava
from meta import Sinleton


class DatabaseHandler(metaclass=Sinleton):
    @exception_logger
    def __init__(self):
        self.db = db
        self.db.connect()
        self.db.create_tables([Movie, Filimo, Namava, FilmNet])

    @exception_logger
    def __save_movie(self, movie):
        movie_instance = Movie.create(caption=movie['caption'])
        movie_instance.save()
        return movie_instance

    @exception_logger
    def insert_movies(self, movies, site):
        for movie in movies:
            if bool(self.__check_movie_exist(movie)):
                instance = eval(site).create(rate=movie['rate'],
                                             movie=self.__check_movie_exist(
                                                 movie))
            else:
                movie_instance = self.__save_movie(movie)
                instance = eval(site).create(rate=movie['rate'],
                                             movie=movie_instance)
            return instance.save()

    @exception_logger
    def __check_movie_exist(self, movie):
        return Movie.get(Movie.caption == movie['caption'])
