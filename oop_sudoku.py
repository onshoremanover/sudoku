#!/usr/local/bin/python3
#
#
#

import pandas as pd
import numpy as np

nr_of_col = 9
nr_of_row = 9
nr_of_depth = 10

class Sudoku():

    init_matrix = np.array([[[3., 0., 0],
                            [0., 1., 0.],
                            [0., 0., 2.]]])

    def create_3d_matrix(depth, row, col):
        """Fills the backtracking matrix with zeros"""
        return np.zeros((depth, row, col))

    def fill_3d_matrix(matrix, depth, row, col, value):
        """Fills any parts with numbers"""
        matrix[depth][row][col]=value
        return matrix

    def put_depth_in_matrix(matrix, depth, row, col, value):
        """Populates the backtracking matrix with increasing numbers as to fill it for checking them later"""
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    matrix[depth+i][row+j][col+k]=value+i
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

    def clear_row(sudoku, row, col):
        """Clears the row"""
        value = int(sudoku[0][row][col])
        print("value von row", value)
        for i in range(0,3):
            print(i,row,col)
            sudoku[value][row][i]=0
        return sudoku

    def clear_col(sudoku, row, col):
        """Clears the cols"""
        value = int(sudoku[0][row][col])
        print("value= ", value)
        for i in range(0,3):
            sudoku[value][i][col]=0
        return sudoku



#   ____
#  |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___
#  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \
#  |  __/| | | (_) | (_| | | | (_| | | | | | |
#  |_ |  |_|  ___ / \__, | _ | __, _ | _ | |_| 
#                   |___/


def main():
    my_matrix = Sudoku()
    my_matrix.__init__
    matrix = my_matrix.create_3d_matrix(row=9, col=9)
    matrix = my_matrix.put_depth_in_matrix(matrix=matrix, depth=0, row=0, col=0, value=0)
    
if __name__ == '__main__':
    main()

