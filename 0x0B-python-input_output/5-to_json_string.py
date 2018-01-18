#!/usr/bin/python3
"""
Module for to_json_string method
"""
import json


def to_json_string(my_obj):
    """
    Method that encodes a string into its json representation
    """
    return json.dumps(my_obj)
