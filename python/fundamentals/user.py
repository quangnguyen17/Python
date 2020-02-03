
class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.current_balance = initial_deposit

    def make_withdrawal(self, amount):
        self.current_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}'s Balance: ${self.current_balance}")

    def transfer_money(self, other_user, amount):
        self.current_balance -= amount
        other_user.receive_money(amount)

    def receive_money(self, amount):
        self.current_balance += amount


quang = User("Quang", 1000)
gaku = User("Gaku", 500)

quang.make_withdrawal(100)
gaku.make_withdrawal(100)

quang.display_user_balance()
gaku.display_user_balance()

quang.transfer_money(gaku, 100)

print("Quang has successfully transfered to Gaku's account $100")
quang.display_user_balance()
gaku.display_user_balance()
