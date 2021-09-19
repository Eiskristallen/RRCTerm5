"""
this module will generate a deck of cards to use
"""
import random

class Card:
    def __init__(self, suit, number):
        """
        The Card class represent a single playing card and it's going to initialised by passing a suit and number 
        """
        self._suit = suit
        self._number = number

    def __repr__(self):
        """
        Return the number and suit of card
        """ 
        # return the number and suit of card
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """
         Get & Set the suit of Card
        """
        return self._suit
    @suit.setter
    def suit(self, suit):
        """
        setter, set the value of suit
        """
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """
        Get & Set the number of Card
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        setter, set the value of number
        """
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    def __init__(self):
        """
        The Deck class represent a bunch of playing cards put in order  
        """
        self._cards = []
        self.populate()

    def populate(self):
        """
        generate a deck of cards
        """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """
        shuffle the cards within deck
        """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """
        remove the card from deck
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        # return the cards that being remove
        return dealt_cards

    def __repr__(self):
        """
        return the number of cards in current deck instance
        """
        cards_in_deck = len(self._cards)
         # return the number of cards within a deck
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)