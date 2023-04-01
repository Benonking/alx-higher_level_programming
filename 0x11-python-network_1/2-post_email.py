#!/usr/bin/python3
"""
Take in email as argument send POST request to it
    isplay the bosy of the rsponse(decoded in utf-8)
"""

from sys import argv
import urllib.parse as parse
import urllib.request as request

if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        r = resp.read()
        print(r.read().decode('utf-8'))
