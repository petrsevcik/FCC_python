
class Category:


    total_balance = 0

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.ledger.append(category)

    def deposit(self, amount, description=""):
        deposit_amount = {"amount":amount, "description":description}
        self.ledger.append(deposit_amount)
        self.balance += amount

    def check_funds(self, amount):
        if amount > self.balance:
            return True
        else:
            return False

    def withdraw(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            purchase = (amount, category)
            self.ledger.append(purchase)
            return True

        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.deposit(amount, description=f"Transfer to {budget_category}")
            budget_category.deposit(amount, description=f"Transfer from {self.category}")
            return True
        else:
            return False

    def __str__(self):
        return 20*"*" + self.category

def create_spend_chart(categories):
    pass

Food = Category("Food")
Gas = Category("Gas")
Party = Category("Cinema")
Food.deposit(1000)
print(Food)