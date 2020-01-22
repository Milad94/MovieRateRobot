from crawl import crawl_filimo, crawl_namava, crawl_filmnet
from database import DatabaseHandler

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    # filimo_data = crawl_filimo()
    # db_handler.insert_movies(movies, site="Filimo")
    # movies = [{'caption': 'cpt', 'rate': 0.7}, {'caption': 'xvb', 'rate': 0.5}]
    movies = crawl_namava()
    db_handler.insert_movies(movies, site="Namava")
    # filmnet_data = crawl_filmnet()
    # db_handler.insert_movies(movies, site="FilmNet")
