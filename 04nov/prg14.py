s="python is a programming language"
search=input("enter search string")
x=s.find(search)
if(x==0):
    print("string found")
else:
    print("not found")