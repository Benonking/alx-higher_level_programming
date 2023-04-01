#!/usr/bin/pyhton3
"""
send request to URL and displays the body
Handle HTTPerror exception and prints Error code:
"""
from sys import argv
from import urllib import request, error

ir __name__ == '__main__':
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as resp:
            rep = resp.read()
            print(rep.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
