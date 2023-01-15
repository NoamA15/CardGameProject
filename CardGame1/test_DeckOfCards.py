from unittest import TestCase, mock
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        """Set up of a deck"""
        self.deck1 = DeckOfCards()
        self.card5 = Card(5, "Diamond")

    def test_init_Valid_length(self):
        """This test checks that the constructor creates a deck of 52 cards"""
        self.assertEqual(52, len(self.deck1.deck))

    # def test_init_Valid_no_doubles(self):

    def test_cards_shuffle_Valid(self):
        """This test checks that the function cards shuffle really shuffles the deck"""
        list1 = self.deck1.deck[:14]
        self.deck1.cards_shuffle()
        list2 = self.deck1.deck[:14]
        self.assertFalse(list1 == list2)
        # print(list1)
        # print(list2)

    def test_deal_one_valid(self):
        """This test checks that deal one removes the card dealt from the deck"""
        self.deck1.deal_one()
        self.assertEqual(51, len(self.deck1.deck))
