#!/usr/bin/python3
"""
Takes ina leter and sends a POST request to http://0.0.0.0:5000/search_user

"""
from sys import argv
import requests
if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dict = req.json()
        if req_dict = {}:
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
