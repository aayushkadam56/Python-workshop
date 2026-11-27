fp=open("exceptiontest.txt","r")
try:
    data=fp.read()
    print(data)
except FileNotFoundError:
    print("file not found")
