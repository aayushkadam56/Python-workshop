#prg for read a file 
fp=open("myfile1.txt","r")
#s=fp.read(4)
#s=fp.read()
#s=fp.readline() #readsingle line from file
s=fp.readlines()#read data in list format
print("data read from file",s)
