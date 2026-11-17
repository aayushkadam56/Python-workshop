#break statement use
n=int(input("enter the limit"))
for i in range(1,n+1):
    #if(i==6):
    #if(i==6 and i==9):
    if(i==6 or i==9):
        break
    print(i,end=" ")
print("loop prg. ends here")