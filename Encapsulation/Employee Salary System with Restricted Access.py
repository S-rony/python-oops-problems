#meduim Hard
# Question 2: Employee Salary System with Restricted Access
# Create a class Employee with private attributes __name, __salary. Add:
    # A method give_raise(percentage) that increases salary by a percentage (only if percentage is positive)
    # A method get_annual_salary() that returns salary * 12
    # Prevent direct modification of salary from outside the class

class Employee():
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def give_raise(self,percentage):
        new_salary = self.__salary + (self.__salary * percentage / 100)
        if new_salary <= 0:
            print("Please write positive amount/percentage")
        else:
            self.__salary = new_salary

    def get_salary(self):
        return self.__salary

    def annual_salary(self):
        return self.__salary * 12

emp = Employee("Sarah", 5000)
print(emp.get_salary())  # 5000

emp.give_raise(10)  # 10% raise
print(emp.get_salary())  # 5500.0

print(emp.annual_salary())  # 66000.0

emp.give_raise(-5)