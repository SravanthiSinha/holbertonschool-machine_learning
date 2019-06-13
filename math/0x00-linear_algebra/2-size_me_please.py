#!/usr/bin/env python3

"""contains a fucntion  that calculates the shape of a matrix"""


def matrix_shape_n(matrix, shape):
    """Recursive function to calculate shape of the matrix"""
    if type(matrix) != list:
        return shape
    else:
        shape.append(len(matrix))
        if type(matrix) == list and len(matrix) > 0:
            matrix_shape_n(matrix[0], shape)


def matrix_shape(matrix):
    """ a function to get shape of the matrix"""
    shape = []
    matrix_shape_n(matrix, shape)
    return shape
