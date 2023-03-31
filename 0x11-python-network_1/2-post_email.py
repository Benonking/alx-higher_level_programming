#!/usr/bin/python3
"""
Take in email as argument send POST request to it
    isplay the bosy of the rsponse(decoded in utf-8)
"""

from sys import argv
from urllib import request, parse

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = parse.urlencode(value)
    data = data.encode('ascii')  # should be bytes
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        r = resp.read()
        print("Your email is: {}".format(r.decode('utf8')))
