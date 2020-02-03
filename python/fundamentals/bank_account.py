
class BankAccount:
    def __init__(self, name, initial_deposit=0, interest_rate=0.01):
        self.name = name
        self.current_balance = initial_deposit
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.current_balance += amount
        return self

    def withdraw(self, amount):
        if self.current_balance <= amount:
            print(
                "You current balance is actually below the amount that you want to withdraw. :(")
            return self

        if amount <= 5:
            print("Insufficient funds: Charging a $5 fee")
            self.current_balance -= (amount + 5)
            return self

        self.current_balance -= amount
        return self

    def yield_interest(self):
        self.current_balance += (self.current_balance * self.interest_rate)
        return self

    def display_account_info(self):
        print(f"{self.name}'s Balance ${self.current_balance}")


first_account = BankAccount("Account 1")
second_account = BankAccount("Account 2")

first_account.deposit(100).deposit(100).deposit(
    100).yield_interest().display_account_info()
second_account.deposit(100).deposit(100).withdraw(50).withdraw(
    20).withdraw(20).withdraw(10).yield_interest().display_account_info()
