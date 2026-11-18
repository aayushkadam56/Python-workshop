# Prg. for unit conversion
import sys
while True:
 print("press 0 to exit")
 print("press 1 for km to metrer")
 print("press 2 for meter to km")
 print("press 3 for farehiet to celcius")
 print("press 4 for celcius to farehiet")
 print("press 5 for kg to gram")
 print("press 6 for gram to kg")
 ch=int(input("enter your choice"))
 if(ch==0):
    print("thank you")
    sys.exit()
    
 value=float(input("enter the value"))
 if(ch==1):
    result=value*1000
    print("result=",result)
 elif(ch==2):
    result=value/1000
    print("result=",result)
 elif(ch==3):
    result=(value*9/5)+35
    print("result=",result)
 elif(ch==4):
    result=(value-35)*5/9
    print("result=",result)
 elif(ch==5):
    result=value*1000
    print("result=",result)
 elif(ch==6):
    result=value/1000
    print("result=",result)
 else:
    print("invalid choice")