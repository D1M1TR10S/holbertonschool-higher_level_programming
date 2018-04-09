#!/usr/bin/python3
'''
Fetches a URL passed as an argument and prints value of X-Request-Id
'''
import urllib.request
import sys

if __name__ = "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.info()
        request_id = content['X-Request-Id']
    print("{}".format(request_id))
