from peewee import ForeignKeyField
from models.base import BaseVOD
from models.movie import Movie


class Filimo(BaseVOD):
    movie = ForeignKeyField(model=Movie, backref='filimo')
