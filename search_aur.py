import sys
import requests
import json
from bs4 import BeautifulSoup

from aur_package import AUR_Package

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: search_aur [PACKAGE_NAME]')
    else:
        url = 'https://aur.archlinux.org/packages'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
        params = {
            'O': 0,
            'K': sys.argv[1]
        }

        aur_query = requests.get(url=url, headers=headers, params=params)
        print(aur_query.text)
