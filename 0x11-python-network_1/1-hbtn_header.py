#!/usr/bin/python3
"""Script sends a request and displays value of X-request-id"""


import urllib.request
import sys

if __name__ == '__main__':
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        data = response.info()

    print(data.get('X-Request-Id'))
