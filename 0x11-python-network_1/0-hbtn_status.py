#!/usr/bin/python3
'''
    Fetching a URL using urllib.request
'''
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()
    decode = content.decode('utf8')
    content_type = type(content)
    print("Body Response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(decode))
