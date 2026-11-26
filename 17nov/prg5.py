keys=["rollno","name","age"]
values=[101,"John",20]
#student={"rollno":101,"name":"John","age":20   }
#zip()-->combines 2 or more iterables.
student=dict(zip(keys,values))
print(student)
