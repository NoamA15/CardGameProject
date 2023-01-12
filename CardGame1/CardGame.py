from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player


class CardGame:
    def __init__(self, p1, num_of_cards_p1, p2, num_of_cards_p2):
        if type(p1) != str:
            raise TypeError('Argument must be of type str')
        if type(p2) != str:
            raise TypeError('Argument must be of type str')
        if type(num_of_cards_p1) != int:
            raise TypeError('Argument must be of type int')
        if type(num_of_cards_p2) != int:
            raise TypeError('Argument must be of type int')
        self.deck = DeckOfCards()
        self.p1 = Player(p1, num_of_cards_p1)
        self.p2 = Player(p2, num_of_cards_p2)
        self.new_game()

    def new_game(self):
        self.deck.cards_shuffle()
        if len(self.p1.hand) > 0 and len(self.p2.hand) > 0:
            raise ValueError('Game has begun')
        self.p1.set_hand(self.deck)
        self.p2.set_hand(self.deck)

    def get_winner(self):
        if len(self.p1.hand) > len(self.p2.hand):
            return f'{self.p1.name} is the FUCKING WINNER!'
        elif len(self.p1.hand) < len(self.p2.hand):
            return f'{self.p2.name} is the FUCKING WINNER!'
        else:
            return None
