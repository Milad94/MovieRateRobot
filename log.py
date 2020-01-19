import logging


def get_logger(file_name):
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)

    file_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s- %(name)s - %(message)s')

    file_handler = logging.FileHandler('log_file.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger
