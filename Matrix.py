import tkinter as tk
from tkinter import messagebox
import numpy as np

#Step 1: -> Writing the logic of the program
def add(a,b):
    return a +b
def subs(a,b):
    return a - b
def dot(a,b):
    return a*b
def inverse(a,b):
    det = np.linalg.det(matrix)
    if det == 0:
        print("Matrix is not invertible determinant is 0")
    else:
        return np.linalg.det(matrix)
#The linalg is a in-built function in numpy, it contains functions of matrix like inverse, determinant, eigenvalues.
def deter(a,b):
    det = np.linalg.det(matrix)


root = tk.Tk()
root.mainloop()