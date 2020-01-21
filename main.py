from crawl import crawl_filimo, crawl_namava, crawl_filmnet
from db_handler import create_tables

if __name__ == "__main__":
    create_tables()
    #filimo_data = crawl_filimo()
    #namava_data = crawl_namava()
    #filmnet_data = crawl_filmnet()


