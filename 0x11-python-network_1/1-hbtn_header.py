#!/usr/bin/python3
"""
Take in URL, sends request and dispys the value of the X-request-Id
    variable found in the header of the resposne
"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print(resp.headers.get("X-Request-Id"))
