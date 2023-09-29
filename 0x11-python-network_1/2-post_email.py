#!/usr/bin/python3
"""
a script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    data = urlencode(data).encode()
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode('UTF-8'))
