#prg for create a file 
fp=open("myfile1.txt","w")
data="""enter data to write in file so that we can acces multiple data simultaniously" \
"for the following dat I will use the following data to write in file\n1.hello\n2.how are you3.I am fine.thank you5.by"""
fp.write(data)
print("file created")
fp.close()
print("file status",fp.closed)