from Card import Card
from DeckOfCards import DeckOfCards
from random import randint


class Player:
    def __init__(self, p_name, number_of_cards):
        if type(p_name) != str:
            raise TypeError("Argument name must be of type str")
        if type(number_of_cards) != int:
            raise TypeError("The number of cards must be of type int")
        if number_of_cards > 26 or number_of_cards < 10:
            self.number_of_cards = 26
        self.name = p_name
        self.number_of_cards = number_of_cards
        self.hand = []

    def set_hand(self, deck: DeckOfCards):
        if type(deck) != DeckOfCards:
            raise TypeError("Argument deck must be of type DeckOfCards")
        for i in range(self.number_of_cards):
            self.hand.append(deck.deal_one())

    def get_card(self, hand: list):
        if type(hand) != list:
            raise TypeError("Argument hand must be of type list")
        return hand.pop(randint(0, self.number_of_cards))

    def add_card(self, card: Card):
        self.hand.append(card)
