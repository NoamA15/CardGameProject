from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        """Set up of a deck"""
        self.deck1 = DeckOfCards()

    def test_init_Valid_length(self):
        """This test checks that the constructor creates a deck of 52 cards"""
        self.assertEqual(52, len(self.deck1.deck))

    #def test_init_Valid_no_doubles(self):


    def test_cards_shuffle_Valid(self):
        """This test checks that the function cards shuffle really shuffles the deck"""
        list1 = self.deck1.deck[:14]
        self.deck1.cards_shuffle()
        list2 = self.deck1.deck[:14]
        self.assertFalse(list1 == list2)
        # print(list1)
        # print(list2)

    # def test_deal_one_Valid(self):
    #     """This test checks that deal one removes the card dealt from the deck"""
    #     deck2 = DeckOfCards()
    #     card = deck2.deal_one()
    #     self.assertNotIn(card, deck2.deck)
    #     print(card)
    #     print(deck2.deck)
