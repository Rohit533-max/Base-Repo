import numpy as np
from typing import List
#asking for number rows and columns
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

#Initializing an empty matrix for storing the values
matrix = []

#Take input row by row
for i in range(row):
    row =[]
    for j in range(col):
        element = int(input(f"Enter the row{i+1},column{j+1} element: "))
        row.append(element)
    matrix.append(row)

#converting the matrix into an array
arr= np.array(matrix)

print(arr)