import pandas as pd
import rlcompleter
import os
import csv
from csv import writer


# reMOVE STUDENT

student_info = pd.read_csv("Studentinfo_t.csv")
print(student_info)

remove_t = str(input("Enter Student ID to remove:"))

stu_new = student_info[student_info['Student ID']== remove_t].index
student_info.drop(stu_new , inplace=True)
df = pd.DataFrame(student_info)
print(df)


# PRINT GRDAE
stuID = str(input("Enter Student ID for results:"))
T1 = pd.read_csv("Studentinfo_t.csv")
T2 = pd.read_csv("marksinfo_t.csv")
t3 = pd.merge(T1, T2, on = "Name")
t4 = t3[t3['Student ID']==stuID]
t4 = pd.DataFrame(t4)
bname = t4["Batch Name"]
suinfo = pd.read_csv("Subjectinfo_t.csv")
suinfot = suinfo[suinfo['Batch Name']== bname]

sinfo = t4[["Student ID","Name","Class Roll Number","Batch Name"]]
sinfo = sinfo.transpose()
minfo = t4.iloc[:,-6:]
minfo = minfo.transpose()
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++ Your Grade Sheet ++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++")     
print(sinfo)
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print(minfo)







