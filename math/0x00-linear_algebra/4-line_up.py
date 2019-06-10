#!/usr/bin/env python3

"""Contains  a function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """
    m = len(arr1)
    result = []
    if (len(arr1) == len(arr2)):
        for x in range(m):
            result.append(arr1[x] + arr2[x])
        return result
    return None
