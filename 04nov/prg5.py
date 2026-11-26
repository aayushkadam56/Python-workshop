# string is palondrome or not
s=input("enter any string:")
res="" 
for x in s:
    res=x+res
print("res=",res)
if (res==s):
    print("string is palondrome-",res)
else:
    print("string is not palondrome-",res)