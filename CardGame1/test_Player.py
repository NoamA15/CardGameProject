from unittest import TestCase
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards
from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Moshe", 26)
        self.deck1 = DeckOfCards()

    def test__init__valid_name(self):
        """This test checks that the player receives his name"""
        self.assertEqual("Moshe", self.player1.name)

    def test__init__valid_num_of_cards1(self):
        """This test checks that the player receives his number of cards (high extreme case)"""
        self.assertEqual(26, self.player1.number_of_cards)

    def test__init__valid_num_of_cards2(self):
        """This test checks that the player receives his number of cards (low extreme case)"""
        player = Player("Moshe", 10)
        self.assertEqual(10, player.number_of_cards)

    def test__init__invalid_name_type(self):
        """This test checks an invalid name type"""
        with self.assertRaises(TypeError):
            Player(123, 20)

    def test__init__invalid_num_of_cards_type(self):
        """This test checks an invalid number of cards type"""
        with self.assertRaises(TypeError):
            Player("Moshe", "abc")

    def test__init__valid_num_of_cards_default(self):
        """This test checks if the number of cards is too high, that the player receives the default number
        (high extreme case)"""
        player = Player("Moshe", 27)
        self.assertEqual(26, player.number_of_cards)

    def test__init__valid_num_of_cards_default_10(self):
        """This test checks if the number of cards is too high, that the player receives the default number
                (low extreme case)"""
        player = Player("Moshe", 9)
        self.assertEqual(26, player.number_of_cards)

    def test__init__valid_hand(self):
        """This test checks that the hand is empty while defining the object 'player'"""
        self.assertEqual([], self.player1.hand)

    def test_set_hand_valid(self):
        """This test checks that he number of cards dealt to the player is the amount he requested"""
        self.player1.set_hand(self.deck1)
        self.assertEqual(self.player1.number_of_cards, len(self.player1.hand))

    def test_set_hand_valid2(self):
        """This test checks that the function adds the card from the deck to the player's hand"""
        with patch('DeckOfCards.DeckOfCards.deal_one') as mock_rand:
            mock_rand.return_value="6: Diamond"
            player = Player("Moshe", 10)
            player.set_hand(self.deck1)
            self.assertEqual(["6: Diamond", "6: Diamond", "6: Diamond", "6: Diamond", "6: Diamond", "6: Diamond",
                              "6: Diamond", "6: Diamond", "6: Diamond", "6: Diamond"], player.hand)

    def test_set_hand_invalid_type(self):
        """This test checks that the function set hands only works with a deck of cards"""
        with self.assertRaises(TypeError):
            self.player1.set_hand(self.player1)

    def test_get_card_valid(self):
        """This test checks that the card was removed from the player's hand after using the 'get card' function"""
        self.player1.set_hand(self.deck1)
        self.player1.get_card(self.player1.hand)
        self.assertEqual(25, len(self.player1.hand))

    def test_get_card_invalid_type(self):
        """This test checks that the function only takes a card from a 'hand' """
        with self.assertRaises(TypeError):
            self.player1.get_card("abc")

    def test_add_card(self):
        """This test checks that the card was added to the player's hand"""
        card = Card(5, "Club")
        self.player1.add_card(card)
        self.assertIn(card, self.player1.hand)

    def test_add_card_invalid_type(self):
        """This test checks that only a 'Card' object can be added to a player's hand"""
        with self.assertRaises(TypeError):
            self.player1.add_card("abc")
