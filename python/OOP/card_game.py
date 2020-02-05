# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [X] build card
# [X] build deck
# [X] implement shuffle
# [ ] implement a sort
# [ ] implement a game

import random


class Card():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
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
        for time in range(random.randint(21, 29)):
            mid = self.deck_length() / 2
            first_half = self.cards[0: int(mid)]
            second_half = self.cards[int(mid): self.deck_length()]
            shuffled_deck = []

            for index in range(len(first_half)):
                shuffled_deck.append(first_half[index])
                shuffled_deck.append(second_half[index])

            self.cards = shuffled_deck

        return self

    def sort(self):
        hearts = []
        clubs = []
        diamonds = []
        spades = []
        # split deck to 4 suit lists
        for card in self.cards:
            if len(self.cards) == 0:
                return self
            elif card.suit == "H":
                hearts.append(card)
            elif card.suit == "C":
                clubs.append(card)
            elif card.suit == "D":
                diamonds.append(card)
            elif card.suit == "S":
                spades.append(card)

        # sort each suit by num
        sorted = False
        counter = 0
        while(sorted == False):
            min = hearts[counter].value
            min_idx = 0
            for idx in range(counter, len(hearts)):
                if min > hearts[idx].value:
                    min = hearts[idx].value
                    min_idx = idx
                    [hearts[counter].value, hearts[min_idx].value] = [
                        hearts[min_idx].value, hearts[counter].value]
            counter += 1
            if counter == len(hearts):
                sorted = True

        sorted = False
        counter = 0
        while(sorted == False):
            min = clubs[counter].value
            min_idx = 0
            for idx in range(counter, len(clubs)):
                if min > clubs[idx].value:
                    min = clubs[idx].value
                    min_idx = idx
                    [clubs[counter].value, clubs[min_idx].value] = [
                        clubs[min_idx].value, clubs[counter].value]
            counter += 1
            if counter == len(clubs):
                sorted = True

        sorted = False
        counter = 0
        while(sorted == False):
            min = diamonds[counter].value
            min_idx = 0
            for idx in range(counter, len(diamonds)):
                if min > diamonds[idx].value:
                    min = diamonds[idx].value
                    min_idx = idx
                    [diamonds[counter].value, diamonds[min_idx].value] = [
                        diamonds[min_idx].value, diamonds[counter].value]
            counter += 1
            if counter == len(diamonds):
                sorted = True

        sorted = False
        counter = 0
        while(sorted == False):
            min = spades[counter].value
            min_idx = 0
            for idx in range(counter, len(spades)):
                if min > spades[idx].value:
                    min = spades[idx].value
                    min_idx = idx
                    [spades[counter].value, spades[min_idx].value] = [
                        spades[min_idx].value, spades[counter].value]
            counter += 1
            if counter == len(spades):
                sorted = True

        # stuff 4 suit lists into deck.cards
        self.cards = []
        for card in hearts:
            self.cards.append(card)
        for card in clubs:
            self.cards.append(card)
        for card in diamonds:
            self.cards.append(card)
        for card in spades:
            self.cards.append(card)
        return self

    def game_poker(self):
        pass

    def game_21(self):
        pass

    def show_deck(self):
        print("*" * 50)
        for card in self.cards:
            card.show_value()
        return self


bicycle_deck = Deck().shuffle().show_deck()
bicycle_deck.sort()
bicycle_deck.show_deck()
