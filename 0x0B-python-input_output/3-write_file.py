#!/usr/bin/python3
"""
This is the module for the write_file method
"""


def write_file(filename="", text=""):
    """
    write_file method that writes string to a file and returns number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
