#!/usr/bin/python3
"""Script sends a request and displays value of X-student-id"""


import urllib.request
import sys

req = sys.argv[1]
with urllib.request.urlopen(req) as response:
    data = response.info()

print(data.get('X-Request-Id'))
