import tkinter as tk
from tkinter import messagebox
import numpy as np


# Create main window
root = tk.Tk()
root.title("Number Input Block")
root.geometry("500x250")


#operations of matrix
def addition():
    try:
        a = read_matrix(matrix1_entries)
        b = read_matrix(matrix2_entries)
        result= np.add(a,b)
        result_label.config(text=f"Additon:\n{result}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def substract():
    try:
        a = read_matrix(matrix1_entries)
        b= read_matrix(matrix2_entries)
        result = np.subtract(a,b)
        result_label.config(text=f"Substraction:\n{result}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def dot_p():
    try:
        a = read_matrix(matrix1_entries)
        b=read_matrix(matrix2_entries)
        result = np.dot(a,b)
        result_label.config(text=f"Dot product\n {result}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def inverse():
    try:
        a = read_matrix(matrix1_entries)
        result = np.linalg.inv(a)
        formatted_result = np.array2string(result, precision=2, suppress_small=True)
        result_label.config(text=f"Inverse:\n{formatted_result}")
    except np.linalg.LinAlgError:
        result_label.config(text="Matrix is singular, cannot invert.")
    except Exception as e:
        result_label.config(text=f"Error:{e}")
    
def determinant():
    try:
       a = read_matrix(matrix1_entries)
       result = np.linalg.det(a)

       result_label.config(text=f"Determinant:\n{result}")
    except Exception as e:
       messagebox.showerror("Input Error", str(e))
       
#storing the entry widgets

matrix1_entries = []
matrix2_entries=[]


#function to read matrix from entry widgets
def read_matrix(entries):

    #infer dimension from number of entries
    #eg 4 entries -> 2x2, 9 entries 3x3
    n = int(len(entries) **0.5)
    matrix=[]
    for i in range(n):
        row =[]
        for j in range(n):
            idx = i *n +j
            text = entries[idx].get().strip()
            if text == "":
                raise ValueError(f"Empty cell at ({i+1}, {j+1}, Please fill all cells)")
            try:
                val = float(text)
            except ValueError:
                raise ValueError(f"Invalid number at ({i+1}, {j+1}): '{text}'")
            row.append(val)
        matrix.append(row)
    return np.array(matrix, dtype=float)

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
tk.Button(root, text="Determinant", command=determinant).place(x=430,y=200)

#Label to show the result
result_label = tk.Label(root, text ="", font = ("Arial",12), justify="left")
result_label.place(x = 100, y=260)


root.mainloop()