#!/usr/local/bin/python3 python3
#
#
#

import pandas as pd
import numpy as np


init_matrix = np.array([[[3., 0., 0.],
                        [0., 1., 0.],
                        [0., 0., 2.]]])

def create_3d_matrix(rows, cols, depth):
    """Fills the backtracking matrix with zeros"""
    return np.zeros((rows, cols, depth))

def fill_3d_matrix(matrix, row, col, depth, value):
    """Fills any parts with numbers"""
    matrix[row][col][depth]=value
    return matrix

def put_depth_in_matrix(matrix, row, col, depth, value):
    """Populates the backtracking matrix with increasing numbers as to fill it for checking them later"""
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                matrix[row+i][col+j][depth+k]=value+i
    return matrix    

def check_if_matrix_is_full(matrix):
    """Check for the beginning if everything the matrix is full"""
    for i in range(1,4):
        for j in range(0,3):
            for k in range(0,3):
                if matrix[i][j][k]==0:
                    return False
    return True

def append_matrix_to_list(sudoku, matrix): 
    """Add the initial matrix to the tot the backtracking matrix""" 
    attached_matrix = np.append(sudoku, matrix, axis=0)
    return attached_matrix 

def check_if_matrix_is_full_and_append(sudoku, matrix):
    """Check for the beginning if everything the matrix is full"""
    for i in range(1,3):
        for j in range(0,2):
            for k in range(0,2):
                if matrix[i][j][k]==0:
                    return False
    return True

def remove_duplicates(sudoku):
    """Removes the duplicates from the backtracking matrix"""
    for i in range(1,4):
        for j in range(0,3):
            for k in range(0,3):
                if sudoku[0][j][k]!=0:
                        sudoku[i][j][k]=0
        
    return sudoku



def clear_col(sudoku, col, depth):
    """Clears the cols"""
    value = sudoku[0][col][depth]
    for i in range(1,4):
        sudoku[i][col][depth]=0
        sudoku[i][col][depth]
    return sudoku

#   ____
#  |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___
#  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \
#  |  __/| | | (_) | (_| | | | (_| | | | | | |
#  |_ |  |_|  ___ / \__, | _ | __, _ | _ | |_| 
#                   |___/


def main():
    matrix=create_3d_matrix(rows=3, cols=3, depth=3)

    matrix=put_depth_in_matrix(matrix=matrix, row=0, col=0, depth=0, value=1)
    matrix1=append_matrix_to_list(sudoku=init_matrix, matrix=matrix)
    check2=check_if_matrix_is_full(matrix=matrix1)
    print(check2)
    check3=check_if_matrix_is_full_and_append(sudoku=init_matrix, matrix=matrix1)
    print(check3)
 
    matrix2=remove_duplicates(sudoku=matrix1)
    print(matrix2)
    print("\nTest 2\n")
    matrix3=clear_col(sudoku=matrix2, col=0, depth=0)
    print(matrix3)


if __name__ == '__main__':
    main()