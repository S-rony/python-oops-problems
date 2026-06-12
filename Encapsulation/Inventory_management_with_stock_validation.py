from idlelib.configdialog import changes

from scipy.special.cython_special import chndtr
# Question 1: Inventory Management with Stock Validation
# Create a class Product with private attributes __name, __price, and __quantity. Add methods to:
    # Get the total value (price * quantity)
    # Update stock (increase/decrease quantity, but quantity should never go negative)
    # Update price (price should never be negative)

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def total_value(self):
        total = self.__price * self.__quantity
        return total

    def update_stock(self, change):
        new_quantity = self.__quantity + change
        if new_quantity <= 0:
            print("Stock cannot be negative!")
        else:
            self.__quantity = new_quantity
    def update_price(self,change):
        new_price = self.__price + change
        if new_price <= 0:
            print("Price cannot be negative!")
        else:
            self.__price = new_price

    def get_details(self):
        return f"{self.__price}: {self.__quantity} units of at ${self.__price} each"



