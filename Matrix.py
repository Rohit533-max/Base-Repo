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
root.geometry("500x250")

label = tk.Label(root,text="Matrix 1")
label.place(x=190,y=30)
# Label
label = tk.Label(root, text="Enter a number:",)
label.place(x=100,y=50)

# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=110,y=70)

#Entry widget2
entry2 = tk.Entry(root, width=10)
entry2.place(x=110,y=100)

#Entry widget3
entry3 = tk.Entry(root, width="10")
entry3.place(x=110,y=130)

#second column

# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=190,y=70)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=190,y=100)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=190,y=130)


#third column
# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=270,y=70)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=270,y=100)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=270,y=130)

#Second matrix
label = tk.Label(root,text="Matrix 1")
label.place(x=190,y=30)
# Label
label = tk.Label(root, text="Enter a number:",)
label.place(x=100,y=50)

# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=110,y=70)

#Entry widget2
entry2 = tk.Entry(root, width=10)
entry2.place(x=110,y=100)

#Entry widget3
entry3 = tk.Entry(root, width="10")
entry3.place(x=110,y=130)

#second matrix---------------------------------------------------------------------------------------------------------------------------------------

label = tk.Label(root,text="Matrix 2")
label.place(x=450,y=30)

# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=390,y=70)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=390,y=100)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=390,y=130)


#third column
# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=470,y=70)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=470,y=100)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=550,y=130)


#second column
# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=550,y=70)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=550,y=100)


# Entry widget (block to write number)
entry = tk.Entry(root, width=10)
entry.place(x=470,y=130)

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

result_label3 = tk.Label(root, text="")
result_label3.pack(pady=5)

root.mainloop()