import unittest

import card_constants as cc
from cards_game import Deck
from cards_game import Card


class DeckTest(unittest.TestCase):
    def test_sorting(self):
        deck = Deck()
        deck.empty()
        deck.add_card(cc.Spades, 2)
        deck.add_card(cc.Diamonds, 5)
        deck.add_card(cc.Spades, cc.King)
        deck.add_card(cc.Hearts, 3)
        deck.add_card(cc.Clubs, cc.Ace)
        # print("initial deck:")
        # deck.print_deck()
        deck.sort()
        # print("deck after sorting:")
        # deck.print_deck()
        # expected: (Spades, 2), (Spades, King), (Diamonds, 5), (Hearts, 3), (Clubs, Ace)
        expected_deck = Deck()
        expected_deck.empty()
        expected_deck.add_card(cc.Spades, 2)
        expected_deck.add_card(cc.Spades, cc.King)
        expected_deck.add_card(cc.Diamonds, 5)
        expected_deck.add_card(cc.Hearts, 3)
        expected_deck.add_card(cc.Clubs, cc.Ace)
        self.assertEqual(deck.deck, expected_deck.deck, "After sorting, deck not as expected")

    def test_add_remove_card(self):
        deck = Deck()
        deck.empty()
        deck.add_card(cc.Spades, 2)
        card = deck.get_card()
        self.assertEqual(len(deck.deck), 0)
        self.assertEqual(card.suit, cc.Spades)
        self.assertEqual(card.rank, 2)

    def test_remove_from_empty_deck(self):
        deck = Deck()
        deck.empty()
        with self.assertRaises(Exception):
            _ = deck.get_card()


class CardTest(unittest.TestCase):
    def test_create_card(self):
        card = Card(cc.Spades, 2)
        self.assertEqual(card.suit, cc.Spades)
        self.assertEqual(card.rank, 2)

    def test_create_invalid_card(self):
        with self.assertRaises(ValueError):
            _ = Card(10, 10)


if __name__ == '__main__':
    unittest.main()
