# Movie Rate Robot

##Project descrption:
To see the description of this project visit [google doc](https://docs.google.com/document/d/1waeA6aBufEDCA4Qty2kNiiYDuxH-RxAoBA8ThovoWCw/edit)

## Step 1:
Create a database in MySQL or PostgresSQL

## Step 2:

Create a local_config.py like this:

```python
DATABASE_CONFIG = {
    'user': ' Your username',
    'passwd': 'Your password',
    'database_name': 'Your database name',
    'host': 'localhost',
    'port': 3306,
    
}
DATABASE_TYPE = "[MYSQL or POSTGRESSQL]"

```


## Step 3:
Run main.py