#!/usr/bin/python3
"""
This is the module for the append_write method
"""


def append_write(filename="", text=""):
    """
    append_write method that appenda string to a file and returns number of characters appended
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
