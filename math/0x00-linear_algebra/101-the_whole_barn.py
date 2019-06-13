#!/usr/bin/env python3
"""contains a function that adds two matrices """

matrix_shape = __import__('2-size_me_please').matrix_shape


def add(mat1, mat2, result, shape, axes, dim):
    """Recursive function to add multidimenional  matrix """
    if type(mat1[0]) == int:
        for x, y in zip(mat1, mat2):
            result.append(x + y)
    elif axes < dim:
        for x in range(shape[axes]):
            k = []
            add(mat1[x], mat2[x], k, shape, axes + 1, dim)
            result.append(k)


def add_matrices(mat1, mat2):
    """ a function that adds 2 matrices """
    shape = matrix_shape(mat1)
    if shape != matrix_shape(mat2):
        return None
    dim = len(shape)
    result = []*dim
    add(mat1, mat2, result, shape, 0, dim)
    return result
