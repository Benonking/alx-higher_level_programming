#!/usr/bin/python3
"""
Takes in ur githhub credentials(Username and password)
    and uses the GITHUB API to access ur id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get('id'))
