#!/usr/bin/python3
"""Script that ensures errors are handled while making request"""


import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
