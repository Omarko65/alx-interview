#!/usr/bin/python3
''' rotates a 2D matrix 90 degrees clockwise '''


def rotate_2d_matrix(matrix):
    ''' function that edits matrix to rotated version '''
    new_matrix = []
    k = len(matrix)

    for i in range(k):
        new_matrix.append([])
    for i in range(k):
        for j in range(k):
            new_matrix[i].insert(0, matrix[j].pop(0))

    for i in range(k):
        matrix[i] = new_matrix[i]
