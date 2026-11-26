#student mrks processing
students=[]#enpty list
while True:
    print("1 for add  student")
    print("2 for display")
    print("0 for exit")
    ch=int(input("enter your choice"))
    if (ch==1):
        name=input("enter student name")
        marks=[]
        for x in range(3):
            m=float(input("enter 3 marks"))
            marks.append(m)
        total=sum(marks)
        per=total/3
        if per>=60:
            div="A division"
        elif per>=50:
            div="B division"
        elif per>=40:
            div="C division"
        else:
            div="fail"
        data1={"name":name,
               "marks":marks,
               "total":total,
               "percentage":per,
               "division":div
               }
        students.append(data1)
        print("record added")
    elif (ch==2):
            if len(students)==0:
                print("no record found")
            else:
             for x in students:
                print("name:",x["name"])
                print("marks:",x["marks"])
                print("total:",x["total"])
                print("percentage:",x["percentage"])
                print("division:",x["division"])
    elif (ch==0):
         break
    else:
        print("invalid choice")