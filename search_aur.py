import sys
import requests
import json
from bs4 import BeautifulSoup

from aur_package import AUR_Package

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: search_aur [PACKAGE_NAME]')
    else:
        # Set headers and request content
        url = 'https://aur.archlinux.org/packages'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
        params = {
            'O': 0,
            'SeB': 'nd',
            'K': sys.argv[1],
            'SB': 'n',
            'SO': 'a',
            'PP': 250,
            'do_Search': 'Go',
        }
        
        # Look up AUR Package
        aur_search = requests.get(url=url, headers=headers, params=params)

        # Parse search results
        aur_results = BeautifulSoup(aur_search.text, 'html.parser')
        aur_packages = []
        
        odd_row = '#pkglist-results-form > table > tbody > tr.odd > td:nth-child(1) > a'
        evn_row = '#pkglist-results-form > table > tbody > tr.even > td:nth-child(1) > a'
        print(aur_results.select(odd_row))
        print(aur_results.select(evn_row))
