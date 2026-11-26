a=(10,20,30,40,50)
print(a)
# a.append(10)  error

b=list(a)  #convert tuple to list
b.append(60)
print(b)

a=tuple(b)  #list to tuple convert
print(a)