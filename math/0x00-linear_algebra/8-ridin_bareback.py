#!/usr/bin/env python3
"""Contains a function that that performs matrix multiplication """


def mat_mul(mat1, mat2):
    """  performs matrix multiplication  """
    result = [[]]
    a = [row[:] for row in mat1]
    b = [row[:] for row in mat2]
    n = len(a[0])
    p = len(b)
    if n == p:
        result = [[sum(a*b for a, b in zip(X, Y)) for Y in zip(*b)] for X in a]
        return result
    return None
