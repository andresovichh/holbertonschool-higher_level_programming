#!/usr/bin/python3
"""
This is a module that fetches a URL"""

import urllib.request
from pprint import pprint



with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print(response.headers.items())