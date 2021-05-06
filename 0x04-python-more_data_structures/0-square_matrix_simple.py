#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(len(matrix)):
        rix = []
        for j in range(len(matrix[i])):
            rix.append(matrix[i][j]**2)
        mat.append(rix)
    return (mat)
