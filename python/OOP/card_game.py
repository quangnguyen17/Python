# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [x] build card
# [x] build deck
# [ ] implement shuffle
# [ ] implement a sort
# [ ] implement a game

import random


class Card():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

        names = {
            1: "C",
            11: "J",
            12: "Q",
            13: "K"
        }

        self.name = names.get(value) or str(value)

    def show_value(self):
        print(f"{self.name} of {self.suit}")


# ace_of_hearts = Card('hearts', 2)
# ace_of_hearts.show_value()

class Deck():
    def __init__(self):
        self.cards = []

        # populate / the cards list
        for suit in ["H", "C", "D", "S"]:
            # build each suit
            # print('suit:"', suit)
            for value in range(1, 14):
                # print('value:"', value)
                # create a card
                self.cards.append(Card(suit, value))

    def deck_length(self):
        return len(self.cards)

    def shuffle(self):
        ranNum = random.randint(1, 10)

        # Determine how many times deck will be shuffled
        time = 0
        while (time < ranNum):
            mid = self.deck_length() / 2
            first_half = self.cards[0: int(mid)]
            second_half = self.cards[int(mid): self.deck_length()]

            shuffled_deck = []

            for index in range(len(first_half)):
                shuffled_deck.append(first_half[index])
                shuffled_deck.append(second_half[index])

            self.cards = shuffled_deck
            time += 1

        return self

    def sort(self):
        pass

    def game(self):
        pass

    def show_deck(self):
        for card in bicycle_deck.cards:
            card.show_value()
        return self


bicycle_deck = Deck().shuffle().show_deck()
