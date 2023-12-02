#!/usr/bin/python3
"""Script that runs a search api"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        query = ""
    else:
        query = sys.argv[1]

    payload = {"q": query}

    res = requests.get('http://0.0.0.0:5000/search_user', data=payload)
    try:
        data = res.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
