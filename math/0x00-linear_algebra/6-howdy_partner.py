#!/usr/bin/env python3

"""Contains a function that concatenates two arrays """


def cat_arrays(arr1, arr2):
    """ concat two arrays element-wise """
    result = []
    result.extend(arr1)
    result.extend(arr2)
    return result
