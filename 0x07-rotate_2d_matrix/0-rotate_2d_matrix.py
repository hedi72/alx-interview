#!/usr/bin/python3
"""This module defines the function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """this function takes as argument
        a matrix of length n*n
        and performs a clockwise rotation"""

    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = temp
