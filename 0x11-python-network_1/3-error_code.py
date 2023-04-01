#!/usr/bin/pyhton3
"""
send request to URL and displays the body
Handle HTTPerror exception and prints Error code:
"""
from sys import argv
from import urllib import request

if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as resp:
            rep = resp.read()
            print(rep.decode('utf8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
