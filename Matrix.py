import numpy as np
from typing import List
#asking for number rows and columns
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

#Initializing an empty matrix for storing the values
matrix = []
matrix2=[]
#Take input row by row
for i in range(row):
    row =[]
    for j in range(col):
        element = int(input(f"Enter the row{i+1},column{j+1} element: "))
        row.append(element)
    matrix.append(row)

#converting the matrix into an array for first matrix
arr= np.array(matrix)
print()
print("Enter the sencond matrix ->")
row2 = int(input("Enter the number of rows: "))
col2 = int(input("Enter the number of columns: "))
#Take input for the second matrix
for i in range(row2):
    row2 =[]
    for j in range(col2):
        element = int(input(f"Enter the row{i+1},column{j+1} element: "))
        row.append(element)
    matrix.append(row2)

#converting the matrix into an array for second martix

arr2 = np.array(matrix2)
