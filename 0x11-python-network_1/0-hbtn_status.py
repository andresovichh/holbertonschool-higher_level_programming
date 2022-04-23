#!/usr/bin/python3
"""
This is a module that fetches a URL"""

import urllib.request



req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print("\t{}".format(type(the_page)))