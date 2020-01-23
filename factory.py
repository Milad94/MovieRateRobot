from crawlers.filimo import FilimoCrawler
from crawlers.filmnet import FilmNetCrawler
from crawlers.namava import NamavaCrawler
from local_config import DATABASE_CONFIG, DATABASE_TYPE
from peewee import MySQLDatabase, PostgresqlDatabase


def database_factory():
    if DATABASE_TYPE == "MYSQL":
        return MySQLDatabase(**DATABASE_CONFIG)
    return PostgresqlDatabase(**DATABASE_CONFIG)


def crawler_factory(name):
    if name == "FILIMO":
        return FilimoCrawler()
    elif name == "NAMAVA":
        return NamavaCrawler()
    return FilmNetCrawler()
