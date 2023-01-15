from Card import Card
from random import shuffle
from random import randint


class DeckOfCards:
    def __init__(self):
        """This function builds the deck"""
        self.deck = []
        self.list1 = ["Diamond", "Spade", "Heart", "Club"]
        for suit in self.list1:
            for value in range(1, 14):
                card1 = Card(value, suit)
                if card1 not in self.deck:
                    self.deck.append(card1)

    def __repr__(self):
        """This function returns the deck with the number and suit of each card"""
        return f"{self.deck}"

    def cards_shuffle(self):
        """This function shuffles the deck"""
        shuffle(self.deck)

    def deal_one(self):
        """This function deals a card"""
        a = randint(0, len(self.deck)-1)
        return self.deck.pop(a)
