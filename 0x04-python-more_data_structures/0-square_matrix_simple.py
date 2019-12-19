#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix.'''

    new_mtx = []

    for mtx in matrix:
        sub = []
        for ele in mtx:
            sub.append(ele**2)
        new_mtx.append(sub)

    return(new_mtx)
