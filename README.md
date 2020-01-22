#Movie Rate Robot

##Step 1:

create a local_config.py like this:

```python
USERNAME = ' Your DB username'
PASSWORD = 'Your DB password!'
DATABASE_NAME = 'Your Database name'
HOST = 'localhost'
PORT = 3306
```

##Step 2:
in main.py un comment this line of codes:
```python
 # namava_data = crawl_namava()
 # db_handler.insert_movies(movies, site="Namava")
```

##Step 3:
run main.py