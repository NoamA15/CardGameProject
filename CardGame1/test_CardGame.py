from unittest import TestCase, mock
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards
from CardGame import CardGame



class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("Ezra", 26, "Noam", 26)

    def test_new_game(self):
        self.fail()

    def test_get_winner(self):
        self.fail()
