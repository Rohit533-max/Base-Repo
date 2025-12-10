# A weather app that fetch real time data of the weather

from tkinter import *
from tkinter import ttk
#calling the Tk inbuilt-class to create a window
root = Tk()

root.title("weather App")
root.geometry("400x400")

root.config(bg="blue")

#creating a label for the heading of the app 
name_label = Label(root, text = "WEATHER APP", font=("Time New Roman", 16, "italic", "bold"))
name_label.place(x=100,y=100, height=60, width=420)

#creating a combo box
list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
com = ttk.Combobox(root,text = "", font=("Time New Roman", 10, "italic"), values= list_name)
com.place(x=200,y=190, width =250, height = 30)

#values in combobox is a build in func that stores the values that are gonna repersent in the options

root.mainloop()