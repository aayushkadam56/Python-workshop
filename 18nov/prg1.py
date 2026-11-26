#Arbitary arguments list funtion
def addition(*x):
    print(type(x))
    print(sum(x))

addition()
addition(10,20)
addition(10,20,30)
addition(10,20,30,40)