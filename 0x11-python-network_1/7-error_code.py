#!/usr/bin/python3
"""Script that fetches an URL and displays the content of the response body
but also handles HTTP Errors printing the error code.

"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.content.decode('utf-8'))
