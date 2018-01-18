#!/usr/bin/python3
"""
Create an object from a string in a json file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file method that creates an object from a json string
    """
    with open(filename, mode='r') as a_file:
        return json.load(a_file)
