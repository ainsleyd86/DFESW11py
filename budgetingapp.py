# Create a Budget class that can instantiate objects 
# based on different budget categories like food,
#  clothing, and entertainment. 
# These objects should allow for depositing and withdrawing 
# funds from each category, 
# as well computing category balances and transferring 
# balance amounts between categories”

class budget:
    def __init__(self, balance):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

food = budget(200)
clothing = budget(100)
entertainment = budget(100)

food.deposit(100)
clothing.deposit(80)
entertainment.deposit(30)

food.withdraw(30)
clothing.withdraw(65.95)
entertainment.withdraw(14.75)

print(food.balance)
print(clothing.balance)
print(entertainment.balance)