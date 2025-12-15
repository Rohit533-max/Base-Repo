# A weather app that fetch real time data of the weather

from tkinter import *
from tkinter import ttk
import os
from dotenv import load_dotenv

#bringing weather api to get real-time data

#requests is a inbuild function that manages to run the url or api's in python
import requests

load_dotenv()
api_key = os.getenv("API_KEY")


def data_get():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
#+ city_name+ to setup the custom city name
#In api data gets in the form of JSON and XML format....
#in JSON data inherit in the dictionary or list form
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre1.config(text=data["main"]["pressure"])

    if data.get("cod") != 200:
        w_label1.config(text="Error")
        wd_label1.config(text=data.get("message", "No data"))
        temp1.config(text="")
        pre1.config(text="")
        return

    # Safe to access weather keys now
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"] - 273.15)))
    pre1.config(text=data["main"]["pressure"])



#calling the Tk inbuilt-class to create a window
root = Tk()

root.title("weather App")
root.geometry("500x600")

root.config(bg="blue")

#creating a label for the heading of the app 
name_label = Label(root, text = "WEATHER APP", font=("Time New Roman", 16, "italic", "bold"))
name_label.place(x=100,y=100, height=40, width=350)

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
city_name = StringVar()
#values in combobox is a build in func that stores the values that are gonna repersent in the options
com = ttk.Combobox(root,text = "", font=("Time New Roman", 12, "italic"), values= list_name, textvariable=city_name)
com.place(x=150,y=190, width =220, height = 30)

#Weather label

#creating the mirroring labels to show the data after fetching

w_label = Label(root, text="Weather Climate", font=("Time New Roman",12, "italic"))
w_label.place(x=120, y= 270, width=150)

w_label1 = Label(root, text="", font=("Time New Roman",12, "italic"))
w_label1.place(x=320, y= 270,width=150)

wd_label = Label(root, text = "Weather Description", font = ("Time New Roman", 10))
wd_label.place(x=120, y=320,width=150)

wd_label1 = Label(root, text = "", font = ("Time New Roman", 10))
wd_label1.place(x=320, y=320,width=150)

temp = Label(root, text = "Temperature: ", font = ("Time New Roman", 10))
temp.place(x=120, y=370,width=150)

temp1 = Label(root, text = "", font = ("Time New Roman", 10))
temp1.place(x=320, y=370, width= 150)

pre = Label(root, text = "Pressure: ", font = ("Time New Roman", 10))
pre.place(x=120, y=420,width=150)

pre1= Label(root, text = "", font = ("Time New Roman", 10))
pre1.place(x=320, y=420, width=150)


#submit button
sub_button = Button(root, text = "Submit", font=("Arial", 10), command=data_get)
sub_button.place(x=270, y=460)

root.mainloop()