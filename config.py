from peewee import MySQLDatabase
from local_config import USERNAME, PASSWORD, DATABASE_NAME

db = MySQLDatabase(database=DATABASE_NAME, user=USERNAME,
                   passwd=PASSWORD, host='localhost',
                   port=3306)
