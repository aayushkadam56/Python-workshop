# list with membership operator
a=[3,23,56,7,8,9]
s=int(input("enter data to search"))
res=s in a
if(res):
    print("data found")
else:
    print("not found")