student = {1: 'arun', 2: 'rollno', 3: 'age'}
try:
      print(student[6])
      #print(student[2])
except KeyError:
      print("key not found")