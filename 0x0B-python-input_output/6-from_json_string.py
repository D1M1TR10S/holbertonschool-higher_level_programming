#!/usr/bin/python3
"""
Module for to_json_string method
"""
import json


def from_json_string(my_str):
    """
    Method that encodes a string into its json representation
    """
    return json.loads(my_str)
