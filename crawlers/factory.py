from crawlers.filimo import FilimoCrawler
from crawlers.filmnet import FilmNetCrawler
from crawlers.namava import NamavaCrawler


def crawler_factory(name):
    if name == "FILIMO":
        return FilimoCrawler()
    elif name == "NAMAVA":
        return NamavaCrawler()
    return FilmNetCrawler()
