#!/usr/bin/python3
"""Script that fetches an URL and displays the content of the response body
but also handles HTTP Errors printing the error code.
"""
from sys import argv
import urllib.error
from urllib.request import (urlopen, Request)

if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as res:
            data = res.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
