#contact book program
contactlist=[]
def addcontact():
    name=input("enter name")
    address=input("enter address")
    emailid=input("enter emailid")
    mobile=input("enter mobile number")
    data={"name":name,"address":address,"emailid":emailid,"mobile":mobile}
    contactlist.append(data)
    print("contact added")

def display():
    if len(contactlist)==0:
        print("contact list is empty")
    else:
        print("===================contact list====================")
        for x in contactlist:
            print("name:",x["name"])
            print("address:",x["address"])
            print("emailid:",x["emailid"])
            print("mobile:",x["mobile"])
            print("-------------------")

def search():
    Name=input("enter name to search")
    for x in contactlist:
        if x["name"]==Name:
            print("name:",x["name"])
            print("address:",x["address"])
            print("emailid:",x["emailid"])
            print("mobile:",x["mobile"])
        else:
            print("contact not found")

while True:
    print("1 for add contact")
    print("2 for display contact")
    print("3 for search contact")
    print("0 for exit")
    choice=int(input("enter your choice"))
    if choice==1:
        addcontact()
    elif choice==2:
        display()
    elif choice==3:
        search()
    elif choice==0:
        break
   