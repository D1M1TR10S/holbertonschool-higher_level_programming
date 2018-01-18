#!/usr/bin/python3
"""
Module to copy an object into a txt file using a json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a string to a txt file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
