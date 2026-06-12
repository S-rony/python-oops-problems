# Question 3: Validation Using Encapsulation
# Create a class Person with a private attribute __age. Add a setter method set_age() that only allows positive values, and a getter get_age().
# Solution:
class Person:
    def __init__(self, age):
        self.__age = age


    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive")

    def get_age(self):
        return self.__age
    

