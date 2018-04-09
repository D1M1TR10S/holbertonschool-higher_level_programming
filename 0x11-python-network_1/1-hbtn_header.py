#!/usr/bin/python3
'''
    Fetches a URL passed as an argument and prints value of X-Request-Id
'''
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    content = str(response.info())
    lines = content.split("\n")
    for line in lines:
        if "X-Request-Id" in line:
            request_id = line.split(" ")[1]
    print(request_id)
