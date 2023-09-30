#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository argv[1] by the user argv[2]
"""

from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = 'https://api.github.com'
    url = '{0}/repos/{1}/{2}/commits'.format(url, username, repo)
    response = requests.get(url)
    obj = response.json()

    for commit in obj[0:10]:
        print(commit['sha'] + ': ' + commit['commit']['author']['name'])
