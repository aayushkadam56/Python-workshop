
# Nested for in loop
n=int(input("enter the no."))
z=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(z,end=" ")
        z+=1
    print()