#!/usr/bin/python3

"""
This is a module that  that takes in a URL, sends a
request to the URL and displays the value of the X-Request-Id
variable found in the header of the response. """

import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    headers = response.getheaders()
    headers = dict(headers)
    print(headers.get('X-Request-Id'))
