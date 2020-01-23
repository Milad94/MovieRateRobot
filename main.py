from database import DatabaseHandler
from factory import crawler_factory


def crawl(site):
    crawler = crawler_factory(site)
    return crawler.get_data()


def save_movies_to_db(movies, site):
    db_handler = DatabaseHandler()
    db_handler.insert_movies(movies, site)


if __name__ == "__main__":
    # filimo_movies = crawl("FILIMO")
    # save_movies_to_db(filimo_movies, "Filimo")

    namava_movies = crawl("NAMAVA")
    save_movies_to_db(namava_movies, "Namava")

    # filmnet_movies = crawl("FILMNET")
    # save_movies_to_db(filmnet_movies, "FilmNet")
