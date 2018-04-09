#!/usr/bin/python3
'''
    Fetches a URL passed as an argument and prints value of X-Request-Id
'''
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    content = str(response.info())
    for line in content.split("\n"):
        if "X-Request-Id" in line:
            request_id = line.split("X-Request-Id: ", 1)[1]
    print(request_id)
