from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame('Ezra', 26, 'Noam', 26)

    def test_init_valid_deck1(self):
        """This test checks that the function dealt the exact amount of cards that the players wanted, """
        game = CardGame('Ezra', 10, 'Noam', 10)
        self.assertEqual(32, len(game.deck.deck))

    def test_init_valid_deck2(self):
        """This test checks that the constructor has dealt the cards to the players"""
        self.assertEqual(0, len(self.game.deck.deck))

    def test_init_valid_player_name(self):
        """This test checks if the player receives his name"""
        self.assertEqual("Ezra", self.game.p1.name)

    def test_init_valid_player_num_of_cards(self):
        """This test checks if the player received the number of cards he wanted"""
        self.assertEqual(26, len(self.game.p1.hand))

    def test_init_invalid_player_name1_type(self):
        """This test checks the type of the player's name"""
        with self.assertRaises(TypeError):
            CardGame(123, 26, 'Noam', 26)

    def test_init_invalid_player_name2_type(self):
        """This test checks the type of the player's name"""
        with self.assertRaises(TypeError):
            CardGame('Ezra', 26, 123, 26)

    def test_init_invalid_player_num_of_cards1_type(self):
        """This test checks the type of the player's number of cards"""
        with self.assertRaises(TypeError):
            CardGame('Ezra', '26', 'Noam', 26)

    def test_init_invalid_player_num_of_cards2_type(self):
        """This test checks the type of the player's number of cards"""
        with self.assertRaises(TypeError):
            CardGame('Ezra', 26, 'Noam', '26')

    def test_init_invalid_player_num_of_cards3_value(self):
        """This test checks the value of the player's number of cards (the value must be equal)"""
        with self.assertRaises(ValueError):
            CardGame('Ezra', 25, 'Noam', 26)

    def test_new_game_invalid(self):
        """This test checks that one cannot start a new game while a game is in progress"""
        with self.assertRaises(ValueError):
            self.game.new_game()

    def test_get_winner_valid_p2_winner(self):
        """This test checks the winner"""
        game1 = CardGame("Ezra", 10, "Noam", 10)
        game1.p1.get_card(game1.p1.hand)
        self.game.get_winner()
        self.assertTrue("Noam", game1.get_winner())

    def test_get_winner_valid_p1_winner(self):
        """This test checks the winner"""
        game1 = CardGame("Ezra", 10, "Noam", 10)
        game1.p2.get_card(game1.p2.hand)
        self.game.get_winner()
        self.assertTrue("Ezra", game1.get_winner())

    def test_get_winner_valid_tie(self):
        """This test checks a tie game"""
        game1 = CardGame("Ezra", 10, "Noam", 10)
        self.game.get_winner()
        self.assertTrue("None", game1.get_winner())


