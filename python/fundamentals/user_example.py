
class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.current_balance = initial_deposit

    def make_deposit(self, amount):
        self.current_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.current_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s Balance: ${self.current_balance}")

    def transfer_money(self, other_user, amount):
        self.current_balance -= amount
        other_user.receive_money(amount)

    def receive_money(self, amount):
        self.current_balance += amount


guido = User("Guido", 0)
guido.make_deposit(100).make_deposit(200).make_deposit(
    300).make_withdrawal(50).display_user_balance()
