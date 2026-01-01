import pandas as pd
import csv

#s_id,fname,lname,class,eng,math,phy,chem,com

df = pd.read_csv("gradebook.csv")
print(df)