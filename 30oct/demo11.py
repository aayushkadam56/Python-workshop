# Nested for in loop
n=int(input("enter the no."))
for i in range(n,0,-1):
    for j in range(1,i+1):
       # print("*",end=" ")
        print(i,end=" ")
        #print(j,end=" ")
    print()