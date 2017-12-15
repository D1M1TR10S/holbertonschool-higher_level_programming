#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in range(len(matrix)):
        newMatrix.append(list(map((lambda x: x * x), matrix[i])))
    return (newMatrix)
