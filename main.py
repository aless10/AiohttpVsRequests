import asyncio

from async_request import request_async, post_async, get_async
from sync import get, post

if __name__ == '__main__':
    URL_LIST = ['https://www.python.org', 'http://httpbin.org']
    result = asyncio.run(request_async(URL_LIST, get_async))
    print(f"Async {result}")
    sync_result = get(URL_LIST)
    print(f"Sync {sync_result}")

    result_post = asyncio.run(request_async(URL_LIST, post_async))
    print(f"Async post {result_post}")
    sync_result_post = post(URL_LIST)
    print(f"Sync post {sync_result_post}")
