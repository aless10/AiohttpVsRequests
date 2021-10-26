import aiohttp

from timer import timer


async def get_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()
            return response.status


async def post_async(url):
    payload = {'key1': 'value1', 'key2': 'value2'}
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=payload) as resp:
            await resp.text()
            return resp.status


@timer
async def request_async(url_list, strategy):
    l = []
    for url in url_list:
        r = await strategy(url)
        l.append(r)
    return l


