# Encapsulation(Accessing certain attributes)
"""
class bank:
    def __init__(self,balance):
        self.__balance=balance 
        # protected attr
    
    def deposit(self, amount):
        self.__balance+=amount
    
    def get_bal(self):
        return self.__balance


ram=bank(1000)
ram.deposit(500)
print(ram.get_bal())

"""
class BankAc:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def get_bal(self):
        return self.__balance

ex1=BankAc(200)
ex1.deposit(50)
print(ex1.get_bal())
