from config import db
from models.filimo import Filimo
from models.filmnet import FilmNet
from models.movie import Movie
from models.namava import Namava


def create_tables():
    db.create_tables([Movie, Filimo, Namava, FilmNet])

