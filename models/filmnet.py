from peewee import ForeignKeyField
from models.base import BaseVOD
from models.movie import Movie


class FilmNet(BaseVOD):
    movie = ForeignKeyField(model=Movie, unique=True, backref='filmnet')
