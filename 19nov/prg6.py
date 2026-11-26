#prg for read a file 
import os
if(os.path.exists("myfile1.txt")):
    x=open("myfile1.txt","r")
    s=x.read()
    print("data read from file",s)
else:
    print("file not found")
fp=open("students.txt","r")
s=fp.read()
print("data read from file",s)
