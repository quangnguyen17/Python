
class User:
    def __init__(self, email):
        self.email = email
        account_one = BankAccount(interest_rate=0.02, initial_deposit=0)
        self.accounts.append(account_one)

    def make_withdrawal(self, account_name, amount):
        for account in self.accounts:
            if account.name == account_name:
                account.withdraw(amount)

    def display_user_balance(self, account_name):
        for account in self.accounts:
            if account.name == account_name:
                account.display_account_info()

    def transfer_money(self, account_name, other_user, amount):
        for account in self.accounts:
            if account.name == account_name:
                # Sending money
                account.current_balance -= amount
                # Receiving, money will be transfered into the first account
                other_user.accounts[0].current_balance += amount

    def add_account(self, new_account):
        self.accounts.append(new_account)


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


# Test Cases
