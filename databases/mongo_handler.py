from databases.factory import database_factory
from databases.handler_interface import DatabaseHandler
from models.mongo import Movie, Filimo, Namava, FilmNet


class MongoDatabaseHandler(DatabaseHandler):
    def __init__(self):
        self.db = database_factory()

    def insert_movies(self, movies, site):
        for movie in movies:
            if not self.select_movie(movie):
                Movie(caption=movie['caption']).save()
                eval(site)(rate=movie['rate']).save()

    def select_movie(self, movie):
        try:
            return Movie.objects(caption=movie['caption']).get()
        except:
            return None
