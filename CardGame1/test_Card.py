from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(1, "Heart")
        self.card5 = Card(5, "Diamond")

    def test__init__valid_value1(self):
        self.assertEqual(1, self.card1.value)

    def test__init__valid_value2(self):
        card2 = Card(13, "Heart")
        self.assertEqual(13, card2.value)

    def test__init__valid_suit(self):
        self.assertEqual("Heart", self.card1.suit)

    def test__init__invalid_value_value1(self):
        with self.assertRaises(ValueError):
            Card(0, "Diamond")

    def test__init__invalid_value_value2(self):
        with self.assertRaises(ValueError):
            Card(14, "Diamond")

    def test__init__invalid_value_type(self):
        with self.assertRaises(TypeError):
            Card("abc", "Diamond")

    def test__init__invalid_suit_value(self):
        with self.assertRaises(ValueError):
            Card(1, "heart")

    def test__init__invalid_suit_type(self):
        with self.assertRaises(TypeError):
            Card(1, 12)

    def test__gt__valid(self):
        card = Card(5, "Heart")
        card2 = Card(8, "Diamond")
        self.assertTrue(card2 > card)

    def test__gt__valid_true_1(self):
        card = Card(5, "Heart")
        self.assertTrue(self.card1 > card)

    def test__gt__valid_false_1(self):
        card = Card(1, "Heart")
        self.assertFalse(self.card5 > card)

    def test__gt__valid_suit_1(self):
        card = Card(5, "Club")
        self.assertTrue(card > self.card5)

    def test__gt__valid_suit_2(self):
        card = Card(5, "Club")
        self.assertFalse(self.card5 > card)

    def test__gt__invalid_other_type(self):
        a = 5
        with self.assertRaises(TypeError):
            self.assertTrue(self.card1 > a)

    def test__eq__valid_true(self):
        card = Card(5, "Heart")
        self.assertTrue(card == self.card5)

    def test__eq__valid_false(self):
        card = Card(5, "Heart")
        self.assertFalse(card == self.card1)

    def test__eq__invalid_other_type(self):
        a = 5
        with self.assertRaises(TypeError):
            self.assertTrue(self.card1 == a)






