#!/usr/bin/env python3
"""contains a function that slices a matrix along a specific axes """


def np_slice(matrix, axes={}):
    """ a function that slices a matrix along a specific axes """
    result = matrix.copy()
    slc = [slice(None)] * len(matrix.shape)
    for axis, s in axes.items():
        slc[axis] = slice(*s)
    return result[tuple(slc)]
