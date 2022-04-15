#!/usr/local/bin/python3
#
#
#

import pandas as pd
import numpy as np

nr_of_col = 9
nr_of_row = 9
nr_of_depth = 10


init_matrix = np.array([[[6., 2., 0.,    3., 4., 5.,    8., 0. ,0.],
                        [ 0., 5., 8.,    7., 2., 6.,    3., 4., 0.],
                        [ 3., 7., 4.,    8., 9., 1.,    2., 5., 6.],

                        [ 4., 3., 0.,    1., 6., 0.,    5., 0., 8.],
                        [ 5., 0., 6.,    4., 7., 0.,    1., 3., 0.],
                        [ 0., 0., 2.,    5., 3., 0.,    0., 6., 4.],

                        [ 8., 6., 5.,    0., 0., 3.,    0., 0., 2.],
                        [ 2., 4., 3.,    6., 0., 7.,    0., 0., 2.],
                        [ 0., 9., 0.,    2., 5., 4.,    6., 8., 3.]]])

def create_3d_matrix(depth, row, col):
    """Fills the backtracking matrix with zeros"""
    return np.zeros((depth, row, col))

def fill_3d_matrix(matrix, depth, row, col, value):
    """Fills any parts with numbers"""
    matrix[depth][row][col]=value
    return matrix

def put_depth_in_matrix(matrix, depth, row, col, value):
    """Populates the backtracking matrix with increasing numbers as to fill it for checking them later"""
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                matrix[depth+i][row+j][col+k]=value+i
    return matrix    

def check_if_matrix_is_full(matrix):
    """Check for the beginning if everything the matrix is full"""
    for i in range(1,10):
        for j in range(0,9):
            for k in range(0,9):
                if matrix[i][j][k]==0:
                    return False
    return True

def append_matrix_to_list(sudoku, matrix): 
    """Add the initial matrix to the tot the backtracking matrix""" 
    attached_matrix = np.append(sudoku, matrix, axis=0)
    return attached_matrix 

def check_if_matrix_is_full_and_append(sudoku, matrix):
    """Check for the beginning if everything the matrix is full"""
    for i in range(1,9):
        for j in range(0,8):
            for k in range(0,8):
                if matrix[i][j][k]==0:
                    return False
    return True

def remove_duplicates(sudoku):
    """Removes the duplicates from the backtracking matrix"""
    for i in range(1,10):
        for j in range(0,9):
            for k in range(0,9):
                if sudoku[0][j][k]!=0:
                        sudoku[i][j][k]=0    
    return sudoku

def clear_row(sudoku, row, col):
    """Clears the row of a single value"""
    value = int(sudoku[0][row][col])
    print("value von row", value)
    if value==0:
        return sudoku
    for i in range(0,9):
        print("Row function: ",i,row,col)
        sudoku[value][row][i]=0
    return sudoku

def clear_col(sudoku, row, col):
    """Clears the cols of a single value"""
    value = int(sudoku[0][row][col])
    print("value= ", value)
    if value==0:
        return sudoku
    for i in range(0,9):
        sudoku[value][i][col]=0
    return sudoku

def clear_row_all(sudoku):
    """Loop function for clearing the rows"""
    for i in range(0,9):
        for j in range(0,9):
            clear_row(sudoku=sudoku, row=i, col=j)
    return sudoku

def clear_col_all(sudoku):
    """Loop function for clearing the cols"""
    for i in range(0,9):
        for j in range(0,9):
            clear_col(sudoku=sudoku, row=i, col=j)
    return sudoku


#   ____
#  |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___
#  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \
#  |  __/| | | (_) | (_| | | | (_| | | | | | |
#  |_ |  |_|  ___ / \__, | _ | __, _ | _ | |_| 
#                   |___/


def main():
    matrix=create_3d_matrix(depth=9, row=9, col=9)

    matrix=put_depth_in_matrix(matrix=matrix, depth=0, row=0, col=0, value=1)
    matrix=append_matrix_to_list(sudoku=init_matrix, matrix=matrix)
 
    matrix=remove_duplicates(sudoku=matrix)
    print(matrix)
    print("\nTest 2\n")

    matrix=clear_row(sudoku=matrix, row=0, col=0)
    print(matrix)
    matrix=clear_col(sudoku=matrix, row=0, col=0)
    print("letzte matrix: ", matrix)

    matrix = clear_row(sudoku=matrix, row=1, col=1)
    matrix = clear_col(sudoku=matrix, row=1, col=1)
    print(matrix)

    matrix = clear_row_all(sudoku=matrix)
    print(matrix)

    matrix = clear_col_all(sudoku=matrix)
    print(matrix)

if __name__ == '__main__':
    main()

