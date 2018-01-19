#!/usr/bin/python3
"""Module for pascal_triangle method
"""


def pascal_triangle(n):
    """
    pascal triangle function that returns a pascal triangle
    """
    arr = []
    if n > 0:
        for y in range(n):
            row = []
            row.append(1)
            if y > 0:
                for x in range(y - 1):
                    row.append(last_row[x] + last_row[x + 1])
                row.append(1)
            arr.append(row)
            last_row = row
    return arr
