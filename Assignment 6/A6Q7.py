class Student:
    pass

class Marks:
    pass

pranav=Student()

pranav_marks=Marks()

print("sambhav is an instance of class Student:",isinstance(pranav,Student))
print("sambhav is an instance of class Marks:",isinstance(pranav,Marks))
print("sambhav_ke_marks is an instance of class Student:",isinstance(pranav_marks,Student))
print("sambhav_ke_marks is an instance of class Marks:",isinstance(pranav_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))
