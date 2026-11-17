#prg. for check given no. is prime or not
n=int(input("enter the no."))
found=0
for i in range(2,n):
    if(n%i==0):
        found=1
        break
if(found==1):
    print("no. is not prime")
else:
    print("no. is prime")