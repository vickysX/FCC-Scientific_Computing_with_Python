import math

class Category:
    def __init__(self, a_category):
        self.budget_category = a_category
        self.ledger = list()
    def deposit(self, amount, description=""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True
    def withdraw(self, amount, description):
        if self.check_funds(amount):
            transaction = {"amount": -amount, "description": description}
            self.ledger.append(transaction)
            return True
        return False
    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            transaction = {"amount": -amount, "description": f"Transfer to {another_category.budget_category}"}
            self.ledger.append(transaction)
            another_category.deposit(amount, f"Transfer from {self.budget_category}")
            return True
        return False
    def __repr__(self):
        str_repr = self.budget_category.center(30, '*') + '\n'
        for transaction in self.ledger:
            the_description = transaction["description"]
            if len(the_description) > 22:
                the_description = the_description[0:22]
            the_amount = "{:.2f}".format(transaction["amount"])
            str_repr += the_description.ljust(22) + the_amount.rjust(7) + '\n'
        str_repr += f"Total: {self.get_balance()}\n"
        return str_repr
    def __str__(self):
        return self.__repr__()


food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
food.deposit(1000.00, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.98, "restaurants and more food")
food.transfer(50.00, clothing)
print(food)

def create_spend_chart(categories):
    percentages = {100: 0, 90: 0, 80: 0, 70: 0, 60: 1, 50: 1, 40: 1, 30: 1, 20: 2, 10: 3, 0: 3} 
    #percentages = dict()
#    for i in range(100, -1, -10):
#        percentages[i] = 0
#    for category in categories:
#        initial_budget = category.ledger[0]["amount"]
#        purchases_sum = 0
#        for i in range(1, len(category.ledger)):
#            if category.ledger[i]["amount"] < 0:
#                purchases_sum += math.abs(category.ledger[i]["amount"])
#            continue
#        percentage = purchases_sum * 100 / initial_budget
#        percentage -= percentage % 10
#        for j in range(percentage, -1, -10):
#            percentages[j] = percentages.get(j, 0) + 1
    print("Percentage spent by category")
    print("100|" + " " + "o  " * percentages[100]) 
    for i in range(90, 0, -10):
        print(f" {i}|" + " " + "o  " * percentages[i])
    print("  0|" + " " + "o  " * percentages[0])
    delimiter = '---' * len(categories) + '-'
    print(f"    {delimiter}")
    maxlen = 0
    for category in categories:
        length = len(category.budget_category)
        if length > maxlen:
            maxlen = length
        elif length < maxlen:
            category.budget_category += ' ' * (maxlen - length)
    for i in range(0, maxlen):
        letter = " " * 5
        for category in categories:
            try:
                letter += category.budget_category[i] + "  "
            except:
                letter += "   "
        print(letter)

create_spend_chart([food, clothing, auto])
