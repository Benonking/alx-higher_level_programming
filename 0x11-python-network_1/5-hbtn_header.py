#!/usr/bin/python3
"""
sends in arequest to a  URL and displays the value of 
    the variable X-Request-Id in the Response header
"""
import requests
from sys import argv 

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))

