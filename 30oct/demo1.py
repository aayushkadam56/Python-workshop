#prg for 1/1!+1/2!+1/31....1/n!
n=int(input("enter the limit"))
sum=0
a=1
f=1
while(a<=n):
 f=f*a
 print("fact=",f)
 div=1/f
 print("div=",div)
 sum=sum+div
 print("sum=",sum)
 a+=1
 print("sum=",sum)