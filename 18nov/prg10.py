import sys

#a=5  #int-28 bytes
#a=5.2 #float-24 bytes
#a=true #bool-28 bytes
#a="xyz#1" #str-41+1char... bytes
a=None #16 bytes
print(sys.getsizeof(a))