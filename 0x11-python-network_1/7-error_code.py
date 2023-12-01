#!/usr/bin/python3
"""Python script that sends a request to the URL and body or error"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
