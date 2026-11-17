
# Nested for in loop
n=int(input("enter the no."))
for i in range(1,n+1):
    #for space
    for k in range(n,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
       
    print()