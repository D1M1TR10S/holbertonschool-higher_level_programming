#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    workMatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            workMatrix = matrix
            group = list(map((lambda x: x * x), workMatrix[i]))
        newMatrix.append(group)
    return (newMatrix)
