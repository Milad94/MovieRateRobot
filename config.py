from peewee import MySQLDatabase
from local_config import USERNAME, PASSWORD

db = MySQLDatabase(database="MovieRateRobot", user=USERNAME,
                   passwd=PASSWORD, host='localhost',
                   port=3306)
