#!/usr/bin/python3
"""
script that takes in a URL, sends a request to theURL and displays
the body of the response.
If the HTTP status code >= 400, it prints: "Error code: HTTP status code"
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    status = response.status_code

    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
