s="logo.jpg"  #sunset .jpg by split
print(s)
a=s.split(".")
print(a)
a[0]="sunset"
s1=a[0]+"."+a[1]
print(s1)

# by replace
s="logo.jpg"
print(s)
s2=s.replace("logo","sunset")
print(s2)