#!/usr/bin/python3
"""
fetch https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    response = r.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
