#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
