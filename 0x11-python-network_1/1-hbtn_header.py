#!/usr/bin/python3
'''
    Fetches a URL passed as an argument and prints value of X-Request-Id
'''
import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.info()
        request_id = content['X-Request-Id']
        print(request_id)
except URLError as e:
    pass
