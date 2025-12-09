import tkinter as tk
from tkinter import messagebox
import numpy as np


# Create main window
root = tk.Tk()
root.title("Number Input Block")
root.geometry("500x250")


#storing the entry widgets

matrix1_entries = []
matrix2_entries=[]
result_label = None


#----------Function to create entry girids dynamically----------
def create_matrix_entries(size):
    global matrix1_entries, matrix2_entries

    #clear old entries
    for e in matrix1_entries + matrix2_entries:
        e.destroy()
    matrix1_entries.clear()
    matrix2_entries.clear()


#Matrix 1
    for i in range(size):
        for j in range(size):
            e = tk.Entry(root,width=10)
            e.place(x=100 + j*80, y =70 + i*30)
            matrix1_entries.append(e)


#Matrix 2
    for i in range(size):
        for j in range(size):
            e = tk.Entry(root, width=10)
            e.place(x=380+ j*80, y = 70 + i*30)
            matrix2_entries.append(e) 

# ----------Helper to read matrix------------

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

#------------------------operations of matrix-------------------
def addition():
    try:
        a = read_matrix(matrix1_entries)
        b = read_matrix(matrix2_entries)
        result= np.add(a, b)
        result_label.config(text=f"Additon:\n{result}")
    except Exception as e:
        messagebox.showerror(" Error", str(e))

def substract():
    try:
        a = read_matrix(matrix1_entries)
        b= read_matrix(matrix2_entries)
        result = np.subtract(a, b)
        result_label.config(text=f"Substraction:\n{result}")
    except Exception as e:
        messagebox.showerror(" Error", str(e))

def dot_p():
    try:
        a = read_matrix(matrix1_entries)
        b=read_matrix(matrix2_entries)
        result = np.dot(a, b)
        result_label.config(text=f"Dot product\n {result}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def inverse():
    try:
        a = read_matrix(matrix1_entries)
        det = np.linalg.det(a)
        if abs(det) < 1e-12:
            result_label.config(text=f"Inverse:\n{np.array2string(result, precision=3)}")
            return 
        result = np.linalg.inv(a)
        result_label.config(text=f"Inverse:\n{np.array2string(result,precision=3)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def determinant():
    try:
       a = read_matrix(matrix1_entries)
       result = np.linalg.det(a)

       result_label.config(text=f"Determinant:\n{result}")
    except Exception as e:
       messagebox.showerror("Input Error", str(e))
       

#-----Dropdown to select matrix size------
def update_size(choice):
    size = int(choice.split("x")[0])  #"2x2" -> 2

    create_matrix_entries(size)

size_var = tk.StringVar(value="3x3")
dropdown = tk.OptionMenu(root,size_var,"2x2","3x3",command=update_size)
dropdown.place(x=100,y=20)



#buttons------------------------------------
tk.Button(root, text = "Add", command=addition).place(x=150, y=200)
tk.Button(root, text="Substract", command=substract).place(x=220,y=200)
tk.Button(root,text="Multiply", command=dot_p).place(x=290,y=200)
tk.Button(root,text ="Inverse", command= inverse).place(x=360,y=200)
tk.Button(root, text="Determinant", command=determinant).place(x=430,y=200)

#Label to show the result
result_label = tk.Label(root, text ="", font = ("Arial",12), justify="left")
result_label.place(x = 100, y=310)

#---Initializing with default 3x3 --------
create_matrix_entries(3)
root.mainloop()