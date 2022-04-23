#!/usr/bin/python3
"""
This is a module that fetches a URL"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode('utf-8')))
