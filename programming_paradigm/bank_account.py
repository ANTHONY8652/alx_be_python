class BankAccount:
    def __init__ (self, initial_balance=0):
        self._account_balance = initial_balance
    
    
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._account_balance
    
    def display_balance(self):
        print["Current balance is ${self.get_balance()}"]