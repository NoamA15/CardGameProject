from Card import Card
from random import shuffle
from random import randint


class DeckOfCards:
    def __init__(self):
        self.deck = []
        self.list1 = ["Diamond", "Spade", "Heart", "Club"]
        for suit in self.list1:
            for value in range(1, 14):
                card1 = Card(value, suit)
                self.deck.append(card1)

    def __repr__(self):
        return f"{self.deck}"

    def cards_shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        a = randint(0, len(self.deck)-1)
        return self.deck.pop(a)
