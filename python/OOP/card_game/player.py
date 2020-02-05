
class Player:
    def __init__(self, name="", hand=[]):
        self.name = name
        self.hand = hand
        self.wins = 0
        self.losses = 0

    def wins(self):
        self.wins += 1
        return self

    def losses(self):
        self.losses += 1
        return self

    def hand(self, cards):
        self.hand = cards
        return self
