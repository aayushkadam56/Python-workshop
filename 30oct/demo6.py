# Exit function  use
import sys
n=int(input("enter the limit"))
for i in range(1,n+1):
    
    if(i==6 ):
       sys.exit("prg. ends here")
    print(i,end=" ")
print("loop prg. ends here")