#!/usr/bin/python3
'''
    Fetch info about a URL using the Requests package and display Request-Id
'''
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
