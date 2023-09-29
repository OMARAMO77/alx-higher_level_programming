#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    auth = (username, password)

    response = requests.get(url, auth)
    obj = response.json()

    print(obj.get('id'))
