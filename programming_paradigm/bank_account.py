class BankAccount:
    def __init__ (self, account_balance: float):
        self.current_balance = account_balance
    
    
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.current_balance:
            self.current_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current balance: ${self.current_balance:.2f}")