import asyncio
import ssl
import timeit
from statistics import mean
from time import time

import aiohttp
import requests

url = 'https://loremflickr.com/320/240/dog'


def load_image(url):
    return requests.get(url, allow_redirects=True)


def write_image(response):
    file_name = response.url.split('/')[-1]
    with open(f'img/{file_name}', 'wb') as file:
        file.write(response.content)


def main():
    for i in range(10):
        write_image(load_image(url))
        print(f'image #{i} was wrote')


def write_image_by_aiohttp(data):
    filename = f'file-{int(time() * 1000)}.jpeg'
    with open(f'img/{filename}', 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True, ssl=ssl.SSLContext()) as response:
        data = await response.read()
        write_image_by_aiohttp(data)


async def main_by_aiohttp():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    sync_timing_results = timeit.repeat(main, repeat=10, number=1)
    sync_timing_avearge = mean(sync_timing_results)
    print(f'{sync_timing_results=}\n{sync_timing_avearge=:.2f}')

    async_timing_results = []
    for i in range(10):
        start_time = time()
        asyncio.run(main_by_aiohttp())
        async_timing_results.append(round(time() - start_time, 2))
    async_timing_average = mean(async_timing_results)
    print(f'{async_timing_results=}\n{async_timing_average=:.2f}')
