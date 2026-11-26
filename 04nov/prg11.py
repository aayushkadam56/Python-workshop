# prg to count no. of words
s=input("enter any string")
print(s)
words=s.split(" ")
print(words)
# print(len(words))
count=0
charcount=0
for x in words:
    count+=1
    charcount+=len(x)
print(" count of words:",count)
print("total char. ",charcount)