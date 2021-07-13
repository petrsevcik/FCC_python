
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        deposit_amount = {"amount":amount, "description":description}
        self.ledger.append(deposit_amount)
        self.balance += amount

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, BudgetCategory):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": "Transfer to {}".format(BudgetCategory.category)})
            self.balance -= amount
            BudgetCategory.ledger.append({"amount": amount, "description": "Transfer from {}".format(self.category)})
            BudgetCategory.balance += amount
            return True
        return False

    def __str__(self):
        result = ''
        result += self.category.center(30, '*') + '\n'
        for item in self.ledger:
            if len(item['description']) > 23:
                result += item['description'][0:23]
            else:
                result += item['description'][0:23].ljust(23)
            result += "{0:.2f}".format(item['amount']).rjust(7)
            result += '\n'
        result += 'Total: {}'.format(self.balance)
        return result


def create_spend_chart(categories):
    s = "Percentage spent by category\n"
    sum = 0
    withdraws = {}
    for x in categories:
        withdraws[x.category] = 0
        for y in x.ledger:
            if y['amount'] < 0:
                withdraws[x.category] += y['amount']
        withdraws[x.category] = -withdraws[x.category]
    for x in withdraws:
        sum += withdraws[x]
    for x in withdraws:
        withdraws[x] = int(withdraws[x] / sum * 100)

    for i in range(100, -10, -10):
        s += str(i).rjust(3) + '| '
        for x in categories:
            if withdraws[x.category] >= i:
                s += 'o  '
            else:
                s += '   '
        s += '\n'
    s += ' ' * 4 + '-' * (1 + len(categories) * 3) + '\n'

    maxlen = 0
    for x in categories:
        if len(x.category) > maxlen:
            maxlen = len(x.category)
    for i in range(maxlen):
        s += ' ' * 5
        for x in categories:
            if len(x.category) > i:
                s += x.category[i] + '  '
            else:
                s += ' ' * 3
        s += '\n'
    return s[0:-1]

