#!/usr/bin/python3
'''
   Sends a GET request to github for a user's id
'''
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    req = requests.get('https://api.github.com/users/{}'.format(sys.argv[1]),
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    data_id = req.json().get('id')
    print(data_id)
