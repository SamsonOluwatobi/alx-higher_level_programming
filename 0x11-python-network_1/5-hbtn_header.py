#!/usr/bin/python3
"""Script that fetches an URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    header = response.headers.get('X-Request-Id')
    print(header)
