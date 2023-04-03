#!/usr/bin/python3
"""
Take in email as argument send POST request to it
    isplay the bosy of the rsponse(decoded in utf-8)
"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
