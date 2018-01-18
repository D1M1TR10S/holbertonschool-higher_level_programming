#!/usr/bin/python3
"""
This is the module for the read_file method
"""


def read_file(filename=""):
    """
    read_file method
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
