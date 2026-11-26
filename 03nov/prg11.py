# packing in tuple
name=("ram","shyam","metha","raj","meena")
print(name)
#(x,y,*z)=name
#(x,*y,z)=name
(*x,y,z)=name
print(x)
print(y)
print(z)