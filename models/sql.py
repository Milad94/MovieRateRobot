from datetime import datetime

from peewee import DateTimeField, Model, FloatField, ForeignKeyField, CharField

from databases.factory import database_factory


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database_factory()

    def save(self, force_insert=False, only=None):
        self.modified_time = datetime.now()
        return super().save(force_insert=False, only=None)


class Movie(BaseModel):
    caption = CharField(max_length=25)


class BaseVOD(BaseModel):
    rate = FloatField()


class Filimo(BaseVOD):
    movie = ForeignKeyField(model=Movie, backref='filimo')


class Namava(BaseVOD):
    movie = ForeignKeyField(model=Movie, backref='namava')


class FilmNet(BaseVOD):
    movie = ForeignKeyField(model=Movie, backref='filmnet')
