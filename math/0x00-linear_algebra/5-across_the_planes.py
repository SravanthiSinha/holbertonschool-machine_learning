#!/usr/bin/env python3

"""Contains  a function that adds two 2D matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """ adds two 2D matrices element-wise """
    result = []
    if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
        for x in range(len(mat1)):
            row = []
            for y in range(len(mat1[0])):
                row.append(mat1[x][y] + mat2[x][y])
            result.append(row)
        return result
    return None
