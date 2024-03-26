#!/usr/bin/python3
"""This module defines the function pascal_triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle.

    Args:
        n (int): The number of rows in the Pascal's Triangle.

    Returns:
        list: A list of lists containing the elements of Pascal's Triangle.
              Each inner list represents a row of the triangle.
    """
    if n <= 0:
        return []

    result_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                result_list[i].append(1)
            else:
                result_list[i].append(
                    result_list[i - 1][j] + result_list[i - 1][j - 1])

    return result_list
