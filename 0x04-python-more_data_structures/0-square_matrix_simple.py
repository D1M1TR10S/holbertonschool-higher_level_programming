#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            group = list(map((lambda x: x * x), matrix[i]))
        newMatrix.append(group)
    return (newMatrix)
