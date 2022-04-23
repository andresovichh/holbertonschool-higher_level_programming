#!/usr/bin/python3
"""
This is a module that fetches a URL"""

import urllib.request



with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()
    print("Body response:")
    print("\t- {}".format(type(response)))
    print("\t- {}".format(response))
    print("\t- {}".format(response.decode('utf-8')))
