from peewee import CharField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField(max_length=25)
