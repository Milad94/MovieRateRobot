from local_config import SQL_DATABASE_CONFIG, MONGO_DATABASE_CONFIG, \
    DATABASE_TYPE
from peewee import MySQLDatabase, PostgresqlDatabase
from mongoengine import connect as MongoDatabase


def database_factory():
    if DATABASE_TYPE == "MYSQL":
        return MySQLDatabase(**SQL_DATABASE_CONFIG)
    elif DATABASE_TYPE == "POSTGRESSQL":
        return PostgresqlDatabase(**SQL_DATABASE_CONFIG)
    return MongoDatabase(**MONGO_DATABASE_CONFIG)


def handler_factory():
    if DATABASE_TYPE == "MONGODB":
        from databases.mongo_handler import MongoDatabaseHandler
        return MongoDatabaseHandler()
    from databases.sql_handler import SQLDatabaseHandler
    return SQLDatabaseHandler()
