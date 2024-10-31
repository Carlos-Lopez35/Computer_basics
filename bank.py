class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.account_balance=0
    def deposit(self, amount):
        if amount <=0:
            return f"The deposit must be higher than 0"
        if amount > 0:
            self.account_balance += amount
            return f"A deposit has been made. The new balance is {self.account_balance} euros."
    def withdraw(self, amount):
        if amount <=0:
            return f"The deposit must be higher than 0"
        if amount > self.account_balance:
            return f"The account does not have enough money"        
        else:
            self.account_balance -= amount 
            return f"A withdraw has been made. The new balance is {self.account_balance} euros."
    def get_balance(self):
        return f"Your current balance is {self.account_balance} euros."
    def __str__(self):
        return f"Account number: {self.account_number}"