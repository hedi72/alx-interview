
#!/usr/bin/python3
""" doc doc doc """


def rotate_2d_matrix(matrix):
    """doc doc doc"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
