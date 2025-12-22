import pandas as pd
import csv
df = pd.read_csv(r"C:\Users\Rohit\OneDrive\Desktop\Git Demo\gradebook.csv")


#Saving students to CSV
def save_to_csv(students,filename ="gradebook.csv"):
    with open(filename, 'w', newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(['StudentID','Class','First_Name','Last_Name','English','Maths','Physics','Chemistry','Computer'])

        for student_id, data in students.items():
            writer.writerow([
                student_id,
                data['Class'],
                data['First_Name'],
                data['Last_Name'],
                data['English'],
                data['Maths'],
                data['Physics'],
                data['Chemistry'],
                data['Computer']
                
            ])

#storing each student as a dictionary into memory
student = []
{
    "id" : "101",
    'class':'10+1',
    'f_name':'X',
    'l_name':'Y',
    'English':"",
    'Maths':"",
    'Physics':"",
    'Chemistry':"",
    'Computer':"",

}

#a function to add the student into file 
def add_student(student):
    student_id = input("Enter student ID: ")
    class_name = input("Enter student class: ")
    first_name = input("Enter first name")
    last_name = input("Enter last name: ")

    while True:
        try:
            e_marks = input("Enter english marks: ")
            
            m_marks = input("Enter maths marks: ")
            
            p_marks = input("Enter physics marks: ")
            
            c_marks = input("Enter chemistry marks: ")
            
            com_marks = input("Enter computer marks: ")
            
        except:
            print("Please enter a valid number!")
        
        student = {
            "id" : student_id,
            'class':class_name,
            'f_name':first_name,
            'l_name':last_name,
            'English':e_marks,
            'Maths':m_marks,
            'Physics':p_marks,
            'Chemistry':c_marks,
            'Computer': com_marks,
        }
