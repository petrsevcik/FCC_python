
class Category:

    ledger = []
    balance = 0

    def __init__(self, category):
        self.ledger.append(category)

    def deposit(self, amount, description=""):
        deposit_amount = {"amount":amount, "description":description}
        self.ledger.append(deposit_amount)
        self.balance += amount

    def withdraw(self, amount, category):
        if self.balance - amount < 0:
            return False
        else:
            self.balance -= amount
            if category not in self.ledger:
                self.ledger.insert(-2,category)
            return True






def create_spend_chart(categories):
    pass

Food = Category("Food")
Gas = Category("Gas")
Party = Category("Cinema")
Food.deposit(1000)
print(Category.ledger)