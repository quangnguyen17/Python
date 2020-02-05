# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [X] build card
# [X] build deck
# [X] implement shuffle
# [ ] implement a sort
# [ ] implement a game

import random
import player


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

    def deck_length(self, addition=0):
        return len(self.cards) + addition

    def shuffle(self):
        for time in range(random.randint(5, 10)):
            mid = self.deck_length() / 2
            first_half = self.cards[0: int(mid)]
            second_half = self.cards[int(mid): self.deck_length()]
            shuffled_deck = []

            for index in range(len(first_half)):
                shuffled_deck.append(first_half[index])
                shuffled_deck.append(second_half[index])

            self.cards = shuffled_deck

        return self

    def random_shuffle(self):
        for time in range(random.randint(self.deck_length(), self.deck_length() * 5)):
            index_one = random.randint(0, self.deck_length(-1))

            while True:
                index_two = random.randint(0, self.deck_length(-1))
                if index_one != index_two:
                    break

            self.cards[index_one], self.cards[index_two] = self.cards[index_two], self.cards[index_one]

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
        hearts = self.sort_suit(hearts)
        clubs = self.sort_suit(clubs)
        diamonds = self.sort_suit(diamonds)
        spades = self.sort_suit(spades)

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

    # helper - given list of cards, sort and return list of cards
    def sort_suit(self, suit):
        answer = []
        while(len(suit) > 0):
            min_idx = 0
            for idx in range(len(suit)):
                if suit[idx].value < suit[min_idx].value:
                    min_idx = idx
            answer.append(suit[min_idx])
            suit.pop(min_idx)
        return answer

    def game(self):

        pass

    def game_21(self):
        is_21 = False

        pass

    def show_deck(self):
        print("*" * 50)
        for card in self.cards:
            card.show_value()
        return self


bicycle_deck = Deck()
bicycle_deck.shuffle().random_shuffle().show_deck()
# bicycle_deck.sort().show_deck()
