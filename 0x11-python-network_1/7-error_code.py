#!/usr/bin/python3
"""
Send request to URL and display body of response
If HTTP status code > 400 print Error code:<value of code>
"""
from sys import argv
import requests

if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
