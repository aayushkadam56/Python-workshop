
try:
    t1=(23,45,67,89,90)
    t1.append(100)
except AttributeError:
    print("tuple is not immutable")
else:
    a=list(t1)
    a.append(100)
    t1=tuple(a)
    print(t1)