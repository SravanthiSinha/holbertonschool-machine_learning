#!/usr/bin/env python3

matrix_shape = __import__('2-size_me_please').matrix_shape

mat1 = []
print(matrix_shape(mat1))
mat2 = [2]
print(matrix_shape(mat2))
mat3 = [2, 3]
print(matrix_shape(mat3))
mat4 = [[1, 2], [3, 4]]
print(matrix_shape(mat4))
mat5 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat5))

mat6 = [[[1, 2, 3], [3, 4, 4], [3, 4, 5]]]
print(matrix_shape(mat6))
