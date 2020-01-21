from decorators import exception_logger


@exception_logger
def parse_page(page_json):
    data = list()
    for movie in page_json['result']:
        data.append(movie['id'])
    return data


@exception_logger
def pars_movie(movie_json):
    data = dict()
    data['caption'] = movie_json['result']['caption'].replace('\u200c', '')
    data['rate'] = movie_json['result']['hit']
    return data
