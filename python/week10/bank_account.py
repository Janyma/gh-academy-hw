class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw_money(self, amount):
        if self.balance<amount:
            print("You dont have enough money in your account")
        else:
            self.balance=self.balance-amount

    def display_balance(self):
        balance_string = "Your balance is %s" % (self.balance)
        return balance_string


account_janyl=BankAccount("Janyl", 1000)
account_janyl.withdraw_money(2000)
account_janyl.deposit(300)
account_janyl.withdraw_money(1200)
print(account_janyl.display_balance())
