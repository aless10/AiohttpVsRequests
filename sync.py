import requests as requests

from timer import timer


@timer
def get(url_list):
    return [requests.get(url).status_code for url in url_list]


@timer
def post(url_list):
    payload = {'key1': 'value1', 'key2': 'value2'}
    return [requests.post('http://httpbin.org/post', data=payload).status_code for url in url_list]
