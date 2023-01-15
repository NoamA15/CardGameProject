from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        """This function sets up 2 different cards"""
        self.card1 = Card(1, "Heart")
        self.card5 = Card(5, "Diamond")

    def test__init__valid_value1(self):
        """This test checks a valid card value (low extreme case)"""
        self.assertEqual(1, self.card1.value)

    def test__init__valid_value2(self):
        """This test checks a valid card value (high extreme case)"""
        card2 = Card(13, "Heart")
        self.assertEqual(13, card2.value)

    def test__init__valid_suit(self):
        """This test checks a valid card suit"""
        self.assertEqual("Heart", self.card1.suit)

    def test__init__invalid_value_value1(self):
        """This test checks an invalid card value (low extreme case)"""
        with self.assertRaises(ValueError):
            Card(0, "Diamond")

    def test__init__invalid_value_value2(self):
        """This test checks an invalid card value (high extreme case)"""
        with self.assertRaises(ValueError):
            Card(14, "Diamond")

    def test__init__invalid_value_type(self):
        """This test checks an invalid card value type"""
        with self.assertRaises(TypeError):
            Card("abc", "Diamond")

    def test__init__invalid_suit_value(self):
        """This test checks an invalid card suit value"""
        with self.assertRaises(ValueError):
            Card(1, "heart")

    def test__init__invalid_suit_type(self):
        """This test checks an invalid card suit type"""
        with self.assertRaises(TypeError):
            Card(1, 12)

    def test__gt__valid(self):
        """This test checks a valid card comparison based on the value of the card"""
        card = Card(5, "Heart")
        card2 = Card(8, "Diamond")
        self.assertTrue(card2 > card)

    def test__gt__valid_true_1(self):
        """This test checks a valid card comparison in the case that one of the cards is an 'Ace' """
        card = Card(5, "Heart")
        self.assertTrue(self.card1 > card)

    def test__gt__valid_false_1(self):
        """This test checks an invalid card comparison in the case that one of the cards is an 'Ace' """
        card = Card(1, "Heart")
        self.assertFalse(self.card5 > card)

    def test__gt__valid_suit_1(self):
        """This test checks a valid card comparison based on the higher suit (2 cards with same value)"""
        card = Card(5, "Club")
        self.assertTrue(card > self.card5)

    def test__gt__valid_suit_2(self):
        """This test checks a valid card comparison based on the higher suit (2 cards with same value) (False case)"""
        card = Card(5, "Club")
        self.assertFalse(self.card5 > card)

    def test__gt__invalid_other_type(self):
        """This test checks an invalid card comparison, the other card's type isn't a 'Card' """
        a = 5
        with self.assertRaises(TypeError):
            self.assertTrue(self.card1 > a)

    def test__eq__valid_true(self):
        """This test checks a valid card comparison"""
        card = Card(5, "Heart")
        card2 = Card(5, "Heart")
        self.assertTrue(card == card2)

    def test__eq__valid_false(self):
        """This test checks a valid false card comparison"""
        card = Card(5, "Heart")
        self.assertFalse(card == self.card1)

    def test__eq__invalid_other_type(self):
        """This test checks an invalid card comparison, the other card's type isn't a 'Card' """
        a = 5
        with self.assertRaises(TypeError):
            self.assertTrue(self.card1 == a)






