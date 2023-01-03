import pandas as pd
import pathlib
import csv
from csv import writer
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")



def stu_info():
    file = pathlib.Path("Students.csv")
    if file.exists ():
        print ("Information on Department Exits")
        print("View the information")
        department = pd.read_csv("Students.csv")
        print(department)
        return stuinformation()
    else:
        color.write("++++++++++++++++++++++++++++++++++++++++++++++++\n","COMMENT")
        color.write("No Prior Information on Students Exits\n","COMMENT")
        color.write("++++++++++++++++++++++++++++++++++++++++++++++++\n","COMMENT")
        print("")
        return stuinformation()
    
def dip_add():
    dip_add = pd.DataFrame(columns=["Student ID ", "Name ","Class Roll Number ","Batch name"])
    parts = int(input("Enter number of students to add:"))

    for _ in range(parts):
        dip = input("Enter Student ID ")
        din = input("Enter Name ")
        bid = input("Enter Class Roll Number ")
        bna = input("Enter Batch name ")
        data = pd.DataFrame({'Student ID':[dip],
                             'Name':[din],
                             'Class Roll Number':[bid],
                             'Enter Batch name':[bna]})
        Student = pd.read_csv("Students.csv")
        if dip in Student.values :
            if din in Student.values :
                if bid in Student.values :
                    print('\n Student and Class Roll Number already exists\n')
                break
            break
        break
    
    data.to_csv('Students.csv', mode='a', index=False, header=False)

    # data.drop_duplicates(keep=False, inplace=True)
    return stuinformation()
def dip_update():
    return stuinformation()

def stuinformation():
    print("================================================")
    print("Welcome to Student Record Management System")
    print("================================================")
    print("Press ")
    print("1 Get Information about Existing Students ")
    print("2 to Add New Students ")
    print("3 Update Students Information")
    print("5 to Exit ")

    ch = int(input("Enter Choice "))
    if ch == 1:
        stu_info()
    elif ch == 2:
        dip_add()
    elif ch ==3:
        dip_update()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")

stuinformation()
