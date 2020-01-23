from datetime import datetime

from peewee import DateTimeField, Model, FloatField
from factory import database_factory


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database_factory()

    def save(self, force_insert=False, only=None):
        self.modified_time = datetime.now()
        return super().save(force_insert=False, only=None)


class BaseVOD(BaseModel):
    rate = FloatField()
