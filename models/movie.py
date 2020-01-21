from peewee import CharField
from models.base import BaseModel


class Movie(BaseModel):
    caption = CharField(max_length=25)
