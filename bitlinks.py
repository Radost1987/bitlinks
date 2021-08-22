import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': url}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers, json=payload
    )
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    headers = {'Authorization': f'Bearer {token}'}
    url_without_scheme = urlparse(link)._replace(scheme='').geturl()
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url_without_scheme}/'
        'clicks/summary',
        headers=headers
    )
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url_without_scheme = urlparse(url)._replace(scheme='').geturl()
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url_without_scheme}',
        headers=headers
    )
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv('TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Input url')
    linkspace = parser.parse_args()
    link_is_bitlink = is_bitlink(bitly_token, linkspace.link)
    try:
        if link_is_bitlink:
            clicks_count = count_clicks(bitly_token, linkspace.link)
            print('Всего кликов ', clicks_count)
        else:
            bitlink = shorten_link(bitly_token, linkspace.link)
            print('Битлинк ', bitlink)
    except requests.exceptions.HTTPError:
        print('Введена неработающая ссылка')
