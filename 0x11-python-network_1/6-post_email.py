#!/usr/bin/python3
"""
send a POst request to URL with the eamil and display Body response
"""
import requests
from sys import argv

if __name__ == '__main__':
    value = {"email": argv[2]}
    req = requests.post(argv[1], data=value)
    print(req.text)
