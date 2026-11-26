#linear /sequential search
a=[2,12,8,9,10,5]
print(a)
found=0
s=int(input("enter sata to be searched"))
for i in range(0,len(a)):
    if(a[i]==s):
        found=1
        break
if(found==1):
        print("element found at-",(i+1))
else:
        print("element not found")