#prg for print div on basis of percentage
per=float(input("enter your percentage"))
if(per>=60):
    print("I division")
elif(per>=45 and per<60):
    print("II division")
elif(per>=33 and per<45):
    print("III division")
else:
    print("fail")