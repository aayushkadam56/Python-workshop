# slicing in list -to get sublist from list
a=[10,20,30,40,50,60,70,80,90,100]
print(a[::])# print all data
print(a[2::])  #print index 2 to all
print(a[-5:-3:])  #print 60 to 70
print(a[0:10:2])  #0 to 9 with step 2
print(a[::-1])   #print list in reverse 
print(a[:5])  # print 0 to 4
del a[0:4]
print(a)