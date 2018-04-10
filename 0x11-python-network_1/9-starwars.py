#!/usr/bin/python3
'''
   Sends a POST request to search names in the Star Wars API
'''
import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get('https://swapi.co/api/people/?search={}'
                           .format(sys.argv[1]))
        data = req.json()
        results = data['results']
        print('Number of results: {}'.format(data['count']))
        for result in results:
            print(result['name'])

    except:
        print('Not a valid JSON')
