#Basic Private Attribute

# Create a class BankAccount with a private attribute __balance. Add a method get_balance() to access it and deposit(amount) to add money to it.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposite(self,amount):
        self.__balance += amount

account = BankAccount(1000)
print(account.get_balance())
account.deposite(100)
print(account.get_balance())


