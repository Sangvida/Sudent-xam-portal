import pandas as pd
import pathlib
import csv
from csv import writer
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")



def dip_info():
    file = pathlib.Path("Department.csv")
    if file.exists ():
        print ("Information on Department Exits")
        print("View the information")
        department = pd.read_csv("Department.csv")
        print(department)
        return dipinformation()
    else:
        color.write("++++++++++++++++++++++++++++++++++++++++++++++++\n","COMMENT")
        color.write("No Prior Information on Department Exits\n","COMMENT")
        color.write("++++++++++++++++++++++++++++++++++++++++++++++++\n","COMMENT")
        print("")
        return dipinformation()
    
def dip_add():
    dip_add = pd.DataFrame(columns=["Department ID ", "Department Name ","Batch ID "])
    parts = int(input("Enter number of departments to add:"))

    for _ in range(parts):
        dip = input("Enter Department ID ")
        din = input("Enter Department Name ")
        bid = input("Enter Batch ID ")
        data = pd.DataFrame({'Department ID':[dip],
                             'Department Name':[din],
                             'Batch ID':[bid]})
        department = pd.read_csv("Department.csv")
        if dip in department.values :
            if din in department.values :
                if bid in department.values :
                    print('\n Department and Batch ID already exists\n')
                break
            break
        break
    
    data.to_csv('Department.csv', mode='a', index=False, header=False)

    # data.drop_duplicates(keep=False, inplace=True)
    return dipinformation()

def course_info_add():
    course_info_add = pd.DataFrame(columns=["Batch ID ", 'Course ID ', 'Course Name '])
    depart = pd.read_csv("Department.csv")
    bid = input('\nEnter the Batch ID for which you want to add Course Information\n')
    if depart['Batch ID'].str.contains(bid).any():
        parts = int(input("Enter number of courses to add:"))

        for _ in range(parts):
            cid = input("Enter Course ID ")
            cin = input("Enter Course Name ")
            data = pd.DataFrame({'Batch ID':[bid],
                                 'Course ID':[cid],
                             'Course Name':[cin]})
            
            data.to_csv('course_info_add.csv', mode='a', index=False, header=False)
    else:
        print('Batch Does Not Exist')
        print('\n You Need to create the Department \ Batch')
        
    return dipinformation()
def dip_update():
    return dipinformation()

def dipinformation():
    print("================================================")
    print("Welcome to Departmental Record Management System")
    print("================================================")
    print("Press ")
    print("1 Get Information about Existing departments ")
    print("2 to Add New Departments ")
    print("3 Update Departmental Information")
    print("4 Add / Update Course Information")
    print("5 to Exit ")

    ch = int(input("Enter Choice "))
    if ch == 1:
        dip_info()
    elif ch == 2:
        dip_add()
    elif ch ==3:
        dip_update()
    elif ch ==4:
        course_info_add()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")

dipinformation()
