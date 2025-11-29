import numpy as np
from typing import List
lis1 = []
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

for i in range(row):
    row = int(input("Enter row values: "))
    lis1.append(row)

ar = np.array(lis1)
print(ar)