#!/usr/bin/env python3
"""Contains a function that concatenates two  matrices along a
specific axis """


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    result = []
    a = [row[:] for row in mat1]
    b = [row[:] for row in mat2]
    m = len(a)
    n = len(a[0])
    p = len(b)
    q = len(b[0])
    if (axis == 1) and (m == p):
        for x in range(len(a)):
            result.append(a[x] + b[x])
    elif (axis == 0) and (n == q):
        result = a + b
    else:
        return None

    return result
