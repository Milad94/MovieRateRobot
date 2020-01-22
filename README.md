# Movie Rate Robot

## Step 1:
Create a database in MySQL

## Step 2:

create a local_config.py like this:

```python
USERNAME = ' Your DB username'
PASSWORD = 'Your DB password!'
DATABASE_NAME = 'Your Database name'
HOST = 'localhost'
PORT = 3306
```

## Step 3:
in main.py uncomment this line of codes:
```python
 # namava_data = crawl_namava()
 # db_handler.insert_movies(movies, site="Namava")
```

## Step 4:
run main.py