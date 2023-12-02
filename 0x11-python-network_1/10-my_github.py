#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""


import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(username, password)
    res = requests.get(url, auth=basic)
    print(res.json().get("id"))
