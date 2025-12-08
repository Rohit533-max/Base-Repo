import tkinter as tk
from tkinter import messagebox
import numpy as np


# Create main window
root = tk.Tk()
root.title("Number Input Block")
root.geometry("500x250")


#operations of matrix
def addition():
    a = read_matrix(matrix1_entries)
    b = read_matrix(matrix2_entries)
    result= np.add(a,b)
    result_label.config(text=f"Additon:\n{result}")

def substract():
    a = read_matrix(matrix1_entries)
    b= read_matrix(matrix2_entries)
    result = np.subtract(a,b)
    result_label.config(text=f"Substraction:\n{result}")

def dot_p():
    a = read_matrix(matrix1_entries)
    b=read_matrix(matrix2_entries)
    result = np.dot(a,b)
    result_label.config(text=f"Dot product\n {result}")

def inverse():
    a = read_matrix(matrix1_entries)
    b = read_matrix(matrix2_entries)
    result0 = np.linalg.inv(a)
    result1 = np.linalg.inv(b)
    result_label.config(text =f"Inverse\n{result0}")
    result_label.config(text=f"Inverse\n{result1}")

#storing the entry widgets
matrix1_entries = []
matrix2_entries=[]


#function to read matrix from entry widgets
def read_matrix(entries):
    matrix=[]
    for i in range(3):
        row =[]
        for j in range(3):
            idx = i *3 +j
            try:
                val = float(entries[idx].get())
            except ValueError:
                val = 0.0
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

#Connecting Entry widgets to Lists

#Matrix 1
for i in range(3):
    for j in range(3):
        e = tk.Entry(root,width=10)
        e.place(x=110 + j*80, y =70 + i*30)
        matrix1_entries.append(e)


#Matrix 2
for i in range(3):
    for j in range(3):
        e = tk.Entry(root, width=10)
        e.place(x=390+ j*80, y = 70 + i*30)
        matrix2_entries.append(e)




#buttons
tk.Button(root, text = "Add", command=addition).place(x=150, y=200)
tk.Button(root, text="Substract", command=substract).place(x=220,y=200)
tk.Button(root,text="Multiply", command=dot_p).place(x=290,y=200)
tk.Button(root,text ="Inverse", command= inverse).place(x=360,y=200)
#Label to show the result
result_label = tk.Label(root, text ="", font = ("Arial",12))
result_label.place(x = 150, y=300)


root.mainloop()