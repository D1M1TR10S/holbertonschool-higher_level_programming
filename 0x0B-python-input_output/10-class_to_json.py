#!/usr/bin/python3
"""Module changing an object to a dict
"""


def class_to_json(obj):
    """
    Turning a class into a json dict
    """
    return (obj.__dict__)
