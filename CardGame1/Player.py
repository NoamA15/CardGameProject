from Card import Card
from DeckOfCards import DeckOfCards
from random import randint


class Player:
    def __init__(self, p_name, number_of_cards):
        """This function defines what the object 'player' consists"""
        if type(p_name) != str:
            raise TypeError("Argument name must be of type str")
        if type(number_of_cards) != int:
            raise TypeError("The number of cards must be of type int")
        if number_of_cards > 26 or number_of_cards < 10:
            self.number_of_cards = 26
        else:
            self.number_of_cards = number_of_cards
        self.name = p_name
        self.hand = []

    def __repr__(self):
        """This function returns the playes name and hand of cards"""
        return f"{self.name}- {self.hand}"

    def set_hand(self, deck: DeckOfCards):
        """This function deals a hand for a player according to the number of cards that has been defined in the
        constructor"""
        if type(deck) != DeckOfCards:
            raise TypeError("Argument deck must be of type DeckOfCards")
        for i in range(self.number_of_cards):
            self.hand.append(deck.deal_one())

    def get_card(self, hand: list):
        """This function removes a card from the player's hand"""
        if type(hand) != list:
            raise TypeError("Argument hand must be of type list")
        return hand.pop(randint(0, len(self.hand)-1))

    def add_card(self, card: Card):
        """This function adds a card to a player's hand"""
        if type(card) != Card:
            raise TypeError("Argument card must be type Card")
        self.hand.append(card)
