# prg. for palandrome no.
n=int(input("Enter no:"))
temp=n
res=0
while(n!=0):
    a=n%10
    res=res*10+a
    n=n//10
if(temp==res):
    print("palandrome no.")
else:
    print("not palandrome no.")