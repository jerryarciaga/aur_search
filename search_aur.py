import sys
import requests
import json

from aur_package import AUR_Package

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: search_aur [PACKAGE_NAME]')
    else:
        # Set headers and request content
        url = 'https://aur.archlinux.org/rpc/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
        params = {
            'v': 5,
            'type': 'search',
            'by': 'name',
            'arg': sys.argv[1],
        }
        
        # Look up AUR Package
        aur_search = requests.get(url=url, headers=headers, params=params)
        
        # Load each result to AUR_Package class
        for result in json.loads(aur_search.text)['results']:
            package = AUR_Package(
                name = result['Name'],
                ver = result['Version'],
                link = result['URL'],
                desc = result['Description'],
                )
            print(package)
