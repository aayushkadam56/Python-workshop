# string with membership operator
s="python is a progrsmming languagre"
search=input("enter search string")
res=search in s
print(res)
if(res):
    print("string found")
else:
    print("not found")