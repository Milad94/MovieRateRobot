from local_config import DATABASE_CONFIG, DATABASE_TYPE
from peewee import MySQLDatabase, PostgresqlDatabase


def database_factory():
    if DATABASE_TYPE == "MYSQL":
        return MySQLDatabase(**DATABASE_CONFIG)
    return PostgresqlDatabase(**DATABASE_CONFIG)
