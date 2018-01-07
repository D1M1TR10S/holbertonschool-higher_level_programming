#!/usr/bin/python3
"""
This is the add_integer module.
It supplies one function, add_integer. For example,

"""
def matrix_divided(matrix, div):
    """
    Return the sum of variables a and b
    """
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) != list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    for y in range(len(matrix)):
        if y > 0:
            if len(matrix[y]) != len(matrix[y - 1]):
                raise TypeError(
                    'Each row of the matrix must have the same size')
        new_row = []
        for x in range(len(matrix[y])):
            if type(matrix[y][x]) != int and\
                    type(matrix[y][x]) != float:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            new_row.append(round((matrix[y][x]/div), 2))
        new_matrix.append(new_row)
    return new_matrix
