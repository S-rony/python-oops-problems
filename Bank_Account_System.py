# Create a BankAccount class.
# Features:
# deposit
# withdraw
# check_balance
# Balance must be private.
from sympy.physics.units import amount


class Bank_Account():
    def __init__(self,name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def check_balance(self):
        print(self.balance)




account_1 = Bank_Account("Soubhik", "2234")
account_1.deposit(200)
account_1.withdraw(50)
account_1.check_balance()




