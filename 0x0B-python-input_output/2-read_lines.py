#!/usr/bin/python3
"""
This is the module for the read_lines method
"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines method that prints nb_lines number of lines to stdout
    """
    line_num = 0
    with open(filename, mode='r', encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                line_num += 1
                if line_num <= nb_lines:
                    print(line, end='')
