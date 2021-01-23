"""
Main module for the cards game. Run play_game() as a demonstration
"""

import random
import card_constants as cc


class Deck:
    """
    Deck, initialized with all cards. Use empty() to clear all and add cards manually.
    Deck is implemented as a list of objects of type Card
    """

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in range(cc.LOWEST_SUIT, cc.HIGHEST_SUIT + 1)
                     for rank in range(cc.LOWEST_RANK, cc.HIGHEST_RANK + 1)]

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self):
        """
        take a card from the stop of the stack and return to the user
        will raise IndexError if the deck is empty
        :return: Card
        """
        card = self.deck.pop()
        return card

    def sort(self):
        self.deck.sort(key=lambda x: (x.suit, x.rank))

    def add_card(self, suit: int, rank: int):
        """
        create a card with the given suit and rank and add it to the deck
        :param suit:
        :param rank:
        :return: None
        """
        card = Card(suit, rank)
        self.deck.append(card)

    def print_deck(self):
        for card in self.deck:
            print(card)

    def empty(self):
        self.deck = []


class Card:
    """
    Card with properties suit and rank, defined in card_constants
    """
    def __init__(self, suit: int, rank: int):
        if suit not in cc.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in cc.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{cc.SUITS[self.suit]}:{cc.RANKS[self.rank]}"

    def __str__(self):
        return f"{cc.SUITS[self.suit]}:{cc.RANKS[self.rank]}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash((self.suit, self.rank))


def get_score_for_cards(player_cards: list):
    return sum([card.suit * card.rank for card in player_cards])


def print_cards(player_cards):
    for card in player_cards:
        print(card)


def play_game():
    deck = Deck()
    deck.shuffle()
    # deck.print_deck()
    p1_cards = []
    p2_cards = []
    times_to_draw = 3
    for _ in range(times_to_draw):
        p1_cards.append(deck.get_card())
        p2_cards.append(deck.get_card())

    p1_value = get_score_for_cards(p1_cards)
    p2_value = get_score_for_cards(p2_cards)
    print("player 1 cards: ")
    print_cards(p1_cards)
    print("player 2 cards: ")
    print_cards(p2_cards)

    if p1_value > p2_value:
        print("player 1 is the winner")
    elif p2_value > p1_value:
        print("player 2 is the winner")
    else:
        print("the game is a draw")


if __name__ == '__main__':
    play_game()
