#prg. for exception handling
try:
   n=5
   m=int(input("enter a no."))
   #res=n/0
   res=n/m
   print(res)
except ZeroDivisionError:
   print("no. must be >zero")
else:
   print("result",res)
finally:
    print ("test program")