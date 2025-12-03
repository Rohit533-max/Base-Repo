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
matrix = []

# Create main window
root = tk.Tk()
root.title("Number Input Block")
root.geometry("300x150")

# Label
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

#Label2
label2 = tk.Label(root, text = "Enter num2")
label2.pack(pady = 10)

#Entry widget2
entry2 = tk.Entry(root, width=100)
entry.pack(pady=5)

# Function to read the number
def get_number():
    try:
        num = float(entry.get())   # convert input to number
        result_label.config(text=f"You entered: {num}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")


#Label to show the result
result_label = tk.Label(root, text ="")
result_label.pack(pady =5)

result_label2 = tk.Label(root, text ="")
result_label2.pack(pady =5)

root.mainloop()