#!/usr/bin/python3
"""
a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    data = {'q': q}
    try:
        response = requests.post(url, data)
        obj = response.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(obj['id'], obj['name']))
    except:
        print('Not a valid JSON')
