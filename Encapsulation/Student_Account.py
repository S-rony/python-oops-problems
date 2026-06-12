# Question 2: Protected Attribute with Setter
# Create a class Student with a protected attribute _name. Add a set_name() method to update it and a get_name() method to retrieve it.
class Student:
    def __init__(self,name):
        self.__name = name


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


student = Student("Soubhik")
student.set_name("rohit")
print(student.get_name())
