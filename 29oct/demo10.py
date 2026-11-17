# prg. to rev of any no.
n=int(input("Enter no:"))
temp=n
rev=0
while(n!=0):
    a=n%10
    rev=rev*10+a
    n=n//10
print("before rev: ",temp)
print("rev: ",rev)