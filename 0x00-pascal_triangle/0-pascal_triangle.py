#!/usr/bin/python3
"""This module defines the function pascal_triangle"""


def pascal_triangle(n):
    """This function return a list of integers representing
        the pascal triangle"""
    if n <= 0:
        return []
    result_list = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0:
                result_list[i].append(1)
            elif j == i:
                result_list[i].append(1)
            else:
                result_list[i].append(
                    result_list[i-1][j] + result_list[i-1][j-1])
    return result_list