#!/usr/bin/python3
'''
   Sends a POST request to a URL with an argument letter as a parameter
'''
import requests
import sys


if __name__ == "__main__":
    value = {'q': ""}
    if len(sys.argv) > 1:
        value['q'] = sys.argv[1]

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=value)
        data = r.json()
        if len(data) == 0:
            print('No result')
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except:
        print('Not a valid JSON')
