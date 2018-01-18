#!/usr/bin/python3
"""
Module for number_of_lines method
"""


def number_of_lines(filename=""):
    """
    number_of_lines method that prints the number of lines in a text file
    """
    line_count = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
        return(line_count)
