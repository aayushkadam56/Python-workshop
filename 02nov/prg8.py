list1=[12,13,54,23,33]
print(list1)
#list2=[13,6,45,34,33]
list2=[list1.copy()]
print(list2)
list2.append(14)
print(list1)
print(list2)
del list1
print(list1)