from unittest import TestCase
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Moshe", 26)
        self.deck1 = DeckOfCards()

    def test__init__valid_name(self):
        self.assertEqual("Moshe", self.player1.name)

    def test__init__valid_num_of_cards1(self):
        self.assertEqual(26, self.player1.number_of_cards)

    def test__init__valid_num_of_cards2(self):
        player = Player("Moshe", 10)
        self.assertEqual(10, player.number_of_cards)

    def test__init__invalid_name_type(self):
        with self.assertRaises(TypeError):
            Player(123, 20)

    def test__init__invalid_num_of_cards_type(self):
        with self.assertRaises(TypeError):
            Player("Moshe", "abc")

    def test__init__valid_num_of_cards_default(self):
        player = Player("Moshe", 27)
        self.assertEqual(26, player.number_of_cards)

    def test__init__valid_num_of_cards_default_10(self):
        player = Player("Moshe", 9)
        self.assertEqual(26, player.number_of_cards)

    def test__init__valid_hand(self):
        list1 = []
        self.assertEqual(list1, self.player1.hand)

    def test_set_hand_valid(self):
        self.player1.set_hand(self.deck1)
        self.assertEqual(self.player1.number_of_cards, len(self.player1.hand))

    def test_set_hand_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player1.set_hand(self.player1)

    def test_get_card_valid(self):
        self.player1.set_hand(self.deck1)
        self.player1.get_card(self.player1.hand)
        self.assertEqual(25, len(self.player1.hand))

    def test_get_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player1.get_card("abc")

    def test_add_card(self):
        card = Card(5, "Club")
        self.player1.add_card(card)
        self.assertIn(card, self.player1.hand)

    def test_add_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player1.add_card("abc")
