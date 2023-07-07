class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = "{:.2f}".format(transaction["amount"])
            items += f"{description:<23}{amount:>7}\n"
            total += transaction["amount"]
        output = title + items + "Total: {:.2f}".format(total)
        return output


def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total_spent = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total_spent -= transaction["amount"]
        spent.append(round(total_spent, 2))
        category_names.append(category.name)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percentage in spent_percentages:
            if percentage >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max([len(name) for name in category_names])

    for i in range(max_name_length):
        graph += "     "
        for name in category_names:
            if i < len(name):
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < max_name_length - 1:
            graph += "\n"

    return graph
