#!/usr/bin/env python3
"""Contains a function that concatenates two matrices along a specific axis"""

matrix_shape = __import__('2-size_me_please').matrix_shape


def cat(mat1, mat2, result, shape, axis, dim):
    """ recursive cat """
    if axis == dim:
        result.extend(mat1)
        result.extend(mat2)
        return
    elif axis < dim:
        for x in range(shape[axis]):
            k = []
            cat(mat1[x], mat2[x], k, shape, axis + 1, dim)
            result.append(k)


def cat_matrices(mat1, mat2, axis=0):
    """ concat two matrices along specific axis"""
    result = []
    m1_s = matrix_shape(mat1)
    m2_s = matrix_shape(mat2)
#    print(m1_s, m2_s)
    if len(m1_s) <= axis or len(m2_s) <= axis:
        """ axis error """
        return None
    if len(m1_s) != len(m2_s):
        """all the input arrays must have same number of dimensions """
        return None
    if m1_s[:axis] != m2_s[:axis] or m1_s[axis+1:] != m2_s[axis+1:]:
        """ all the input array dimensions except
        for the concatenation axis must match exactly"""
        return None
    cat(mat1, mat2, result, m1_s, 0, axis)
    return result
