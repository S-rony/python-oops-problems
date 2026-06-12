#medium type
# Create a class Temperature with a private attribute __celsius. Add:
    # A method set_temperature(value, unit) that accepts temperature in "C" or "F" and converts/stores it as Celsius
    # A method get_celsius() and get_fahrenheit() to retrieve the value in respective units
    # Validate that the unit is either "C" or "F", otherwise print an error
from anyio import value


class Temperature:
    def __init__(self):
        self.__celsius = 0


    def set_temperature(self,value,unit):
        if unit == "C":
            self.__celsius = value
        elif unit == "F":
            self.__celsius = (value - 32) * 5/9
        else:
            print("Invalid unit! Use 'C' or 'F'.")

    def get_celsius(self):
        return round(self.__celsius,2)

    def get_fahrenheit(self):
        return round((self.__celsius*9/5) + 32, 2)

temp = Temperature()
temp.set_temperature(100, "F")
print(temp.get_celsius())      # 37.78
print(temp.get_fahrenheit())   # 100.0

temp.set_temperature(25, "C")
print(temp.get_celsius())      # 25
print(temp.get_fahrenheit())   # 77.0

temp.set_temperature(50, "K")  #