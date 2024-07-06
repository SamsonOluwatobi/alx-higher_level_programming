#!/usr/bin/python3
"""Script that fetches an URL and sends an email as data using a POST request

"""
from sys import argv
from requests import post

if __name__ == "__main__":
    (url, email) = argv[1:3]
    response = post(url, data={'email': email})
    print(response.content.decode('utf-8'))
