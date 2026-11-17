# Armstrong no.
n=int(input("Enter any no.:"))
res=0
temp=n
while(n!=0):
 a=n%10
 res=res+(a**3)
 n=n//10
if(res==temp):
    print("Armstrong no.")
else:
    print("Not an Armstrong no.")