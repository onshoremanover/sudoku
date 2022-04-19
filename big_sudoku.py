#!/usr/local/bin/python3
#
#
#

from numpy.core.fromnumeric import trace
import pandas as pd
import numpy as np

init_matrix = np.array([[[8., 0., 0.,    0., 0., 0.,    0., 0. ,0.],
                        [ 0., 0., 3.,    6., 0., 0.,    0., 0., 0.],
                        [ 0., 7., 0.,    0., 9., 0.,    2., 0., 0.],

                        [ 0., 5., 0.,    0., 0., 7.,    0., 0., 0.],
                        [ 0., 0., 0.,    0., 4., 5.,    7., 0., 0.],
                        [ 0., 0., 0.,    1., 0., 0.,    0., 3., 0.],

                        [ 0., 0., 1.,    0., 0., 0.,    0., 6., 8.],
                        [ 0., 0., 8.,    5., 0., 0.,    0., 1., 0.],
                        [ 0., 9., 0.,    0., 0., 0.,    4., 0., 0.]]])
                        

def create_3d_matrix(row, col, depth):
    """Creates the 3d matrix"""
    return np.zeros((row, col, depth))

def put_depth_in_matrix(matrix, depth, row, col, value):
    """Populates the backtracking matrix with increasing numbers as to fill it for checking them later"""
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                matrix[depth+i][row+j][col+k]=value+i
    return matrix    

def append_matrix_to_list(sudoku, matrix): 
    """Add the initial matrix to the front of the backtracking matrix""" 
    attached_matrix = np.append(sudoku, matrix, axis=0)
    return attached_matrix 

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
    #print("value von row", value)
    if value==0:
        return sudoku
    for i in range(0,9):
        sudoku[value][row][i]=0
    return sudoku

def clear_col(sudoku, row, col):
    """Clears the cols of a single value"""
    value = int(sudoku[0][row][col])
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

def depth_unique(sudoku, row, col,):
    """Counts the unique numbers in the depth"""
    value = int(sudoku[0][row][col])
    a_list = []
    if value!=0:
        return sudoku
    for i in range(1,10):
        # Skips if it is a zero
        if sudoku[i][row][col]==0:
            continue
        # Counts the unique numbers in the depth
        a_list.append(i)
        #print(a_list) 
    if len(a_list)==1:
        sudoku[0][row][col]=a_list[0]
        #f"Sudoku:  {a_list}"
        print("Sudoku:  ", a_list, "at position ",col,"",row)
    
    return sudoku

def depth_unique_all(sudoku):
    """Loop function for checking the unique numbers in the depth"""
    for i in range(0,9):
        for j in range(0,9):
            depth_unique(sudoku=sudoku, row=i, col=j)
    return sudoku

def minisquare(sudoku, row, col):
    """Checks the minisquare"""
    value = int(sudoku[0][row][col])
    if value == 0:
        return sudoku
    
    klein = range(0,3)
    mittel = range(3,6)
    gross = range(6,9)  

    if row in klein and col in klein:
        sudoku[value,0:3,0:3]=0
        return sudoku
    elif row in klein and col in mittel:
        sudoku[value,0:3,3:6]=0
        return sudoku
    elif row in klein and col in gross:
        sudoku[value,0:3,6:9]=0
        return sudoku
    elif row in mittel and col in klein:
        sudoku[value,3:6,0:3]=0
        return sudoku
    elif row in mittel and col in mittel:
        sudoku[value,3:6,3:6]=0
        return sudoku
    elif row in mittel and col in gross:
        sudoku[value,3:6,6:9]=0
        return sudoku
    elif row in gross and col in klein:
        sudoku[value,6:9,0:3]=0
        return sudoku
    elif row in gross and col in mittel:
        sudoku[value,6:9,3:6]=0
        return sudoku
    elif row in gross and col in gross:
        sudoku[value,6:9,6:9]=0
        return sudoku
    return sudoku
  
def minisquare_all(sudoku):
    """Loop function for the minisquare"""
    for i in range(0,9):
        for j in range(0,9):
            minisquare(sudoku=sudoku, row=i, col=j)
    return sudoku

def exclude_row(sudoku):
    """Exclude the minisquare"""
    for row in range(0,9):
        for depth in range(1,9):
            if sudoku[depth][row][sudoku[depth][row] != 0].size == 1:
                index = np.where(sudoku[depth][row] == depth)
                for i in range(1,9):
                    if i != depth:
                        sudoku[i][row][index[0]] = 0
    return sudoku

def exclude_col(sudoku):
    """Exclude the minisquare"""
    #alle col durchgehen
    for col in range(0,9):
        #backtracking depth durchgehen
        for depth in range(1,9):
            #wenn es nur ein eintrag in der depth gibt
            if sudoku[depth][sudoku[depth][0:9][col] != 0].size == 1:
                #index des eintrags in der depth
                index = np.where(sudoku[depth][0:9][col] == depth)
                #alle depth durchgehen
                for i in range(1,9):
                    if i != depth:
                        #wenn die depth nicht die gleiche ist wie die depth
                        #dann wird der eintrag in der depth Null gesetzt
                        sudoku[i][index[0]][col] = 0
    return sudoku
    



  

def trial(sudoku):
    sudoku = remove_duplicates(sudoku=sudoku)
    sudoku = clear_row_all(sudoku=sudoku)
    sudoku = clear_col_all(sudoku=sudoku)
    sudoku = minisquare_all(sudoku=sudoku)
    sudoku = depth_unique_all(sudoku=sudoku)
    sudoku = exclude_col(sudoku=sudoku)
    sudoku = exclude_row(sudoku=sudoku)
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
 
    for i in range(0,20):
        print("Trail: ", i+1)
        matrix=trial(sudoku=matrix)
    print(matrix[0])
        





if __name__ == '__main__':
    main()
