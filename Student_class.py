from six import print_


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def print_q(self):
        print("Name", self.name)
        print("Name", self.age)

student_1 = Student("soubhik",25)
student_2 = Student("Vivek", 23)

student_1.print_q()
student_2.print_q()