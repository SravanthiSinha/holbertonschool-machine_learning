#!/usr/bin/env python3

"""Contains  a function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """ returns the transpose of a 2D matrix, matrix """
    matrix_t = []
    m = len(matrix)
    n = len(matrix[0])
    for x in range(0, n):
        row = []
        for y in range(0, m):
            row.append(matrix[y][x])
        matrix_t.append(row)
    return matrix_t
