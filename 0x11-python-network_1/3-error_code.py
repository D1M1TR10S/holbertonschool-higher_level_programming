#!/usr/bin/python3
'''
    Retrieving data from a URL and raising error on failure
'''
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf8')
        print(content)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
