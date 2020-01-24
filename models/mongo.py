from datetime import datetime

from mongoengine import DateTimeField, StringField, FloatField, Document, \
    ReferenceField


class Movie(Document):
    caption = StringField()
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None,
             **kwargs
             ):
        self.modified_time = datetime.now()
        return super().save()


class Filimo(Document):
    movie = ReferenceField(Movie)
    rate = FloatField()
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None,
             **kwargs
             ):
        self.modified_time = datetime.now()
        return super().save()


class Namava(Document):
    movie = ReferenceField(Movie)
    rate = FloatField()
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None,
             **kwargs
             ):
        self.modified_time = datetime.now()
        return super().save()


class FilmNet(Document):
    movie = ReferenceField(Movie)
    rate = FloatField()
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, signal_kwargs=None,
             **kwargs
             ):
        self.modified_time = datetime.now()
        return super().save()
