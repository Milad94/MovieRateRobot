from peewee import MySQLDatabase
from local_config import USERNAME, PASSWORD, DATABASE_NAME, HOST, PORT

db = MySQLDatabase(database=DATABASE_NAME, user=USERNAME,
                   passwd=PASSWORD, host=HOST,
                   port=PORT)
