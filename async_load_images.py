import timeit

import requests


def load_image(url):
    return requests.get(url, allow_redirects=True)


def write_image(response):
    file_name = response.url.split('/')[-1]
    with open(f'img/{file_name}', 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://loremflickr.com/320/240/dog'
    for i in range(10):
        write_image(load_image(url))
        print(f'image #{i} was wrote')


if __name__ == '__main__':
    print(timeit.repeat(main, repeat=10, number=1))
