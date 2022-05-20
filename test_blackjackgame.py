import unittest
import random


class TestProgram(unittest.TestCase):
    def test_input(self):
        """
        Test that input is yes or no
        """
        hit = input("Would you like hit? Yes or No").lower()
        result = input(yes, no)
        self.assertIs(result, yes, no)


    def test_suite(self):
        """
        Test that the suite has hearts
        """

        self.deck = {
            "club": None,
            "hearts": None,
            "diamonds": None,
            "spades": None,
        }
    dealer_cards = []
    players_cards = []

    def cards(self):
        cards = [card for card in range(2, 14)]
        for suite in self.deck:
            self.deck[suite] = cards

            result = self.deck[suite] = cards
            self.assertIsInstance(cards, suite)

    def test_type(self):
        """
        Test that the cards are a list
        """
        self.dealer_cards = [[random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))]]
        result = [[random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))]]
        self.assertTrue(result, list)

    def dictionary_lenght(self):
        """
        Test that the length of the dictionary is 4
        """

        self.deck = {
            "club": None,
            "hearts": None,
            "diamonds": None,
            "spades": None,
        }

        
        result = len(self.deck, 4)
        self.assertIs(result, 4)


if __name__ == '__main__':
    unittest.main()

