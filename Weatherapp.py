# A weather app that fetch real time data of the weather

from tkinter import *
from tkinter import ttk

#bringing weather api to get real-time data

#requests is a inbuild function that manages to run the url or api's in python
import requests

city_name = "himachal pradesh"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_name+"&appid=729749090ab85fd365c779cc7443a766").json()
#+ city_name+ to setup the custom city name
#In api data gets in the form of JSON and XML format....
#in JSON data inherit in the dictionary or list form

print(data)








#calling the Tk inbuilt-class to create a window
root = Tk()

root.title("weather App")
root.geometry("600x600")

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
#values in combobox is a build in func that stores the values that are gonna repersent in the options
com = ttk.Combobox(root,text = "", font=("Time New Roman", 12, "italic"), values= list_name)
com.place(x=200,y=190, width =250, height = 30)

#submit button
sub_button = Button(root, text = "Submit", font=("Arial", 10))
sub_button.place(x=300, y=250)


#Weather label

#creating the mirroring labels to show the data after fetching

w_label = Label(root, text="Weather Update", font=("Time New Roman", 20, "bold", "italic"))
w_label.place(x=120, y= 300)

wd_label = Label(root, text = "Weather Description", font = ("Time New Roman", 10))
wd_label.place(x=120, y=350)

temp = Label(root, text = "Temperature: ", font = ("Time New Roman", 10))
temp.place(x=120, y=400)

temp1 = Label(root, text = "T", font = ("Time New Roman", 10))
temp1.place(x=240, y=400, width= 250)

pre = Label(root, text = "Pressure: ", font = ("Time New Roman", 10))
pre.place(x=120, y=450)

pre1= Label(root, text = "P", font = ("Time New Roman", 10))
pre1.place(x=240, y=450, width=250)

root.mainloop()