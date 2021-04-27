class Budget:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        # this should return a True or False, it checks if amount is less or greater than self.amount
        if self.amount >= amount:
            return True
        elif self.amount < amount:
            return False

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)

    def transfer(self, category, amount):
        # transfer between two instantiated categories
        return self.withdraw(amount) + ', ' + category.deposit(amount)


food_category = Budget("Food", 0)
clothing_category = Budget("Clothing", 300)
car_category = Budget("Car Expenses", 600)

print(food_category.deposit(500))
print(food_category.withdraw(250))
print(food_category.budget_balance())
print(food_category.check_balance(0))
print(food_category.transfer(car_category, 50))
print(food_category.budget_balance())
print(car_category.budget_balance())
