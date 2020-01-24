# Step 1: Import the random module.
# This will be used to shuffle the deck prior to dealing.
# Then, declare variables to store suits, ranks and values.
# You can develop your own system, or copy ours below.
# Finally, declare a Boolean value to be used to control while loops.
# This is a common practice used to control the flow of the game.

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Class Definitions
# Consider making a Card class where each Card object has a suit and a rank,
# then a Deck class to hold all 52 Card objects, and can be shuffled,
# and finally a Hand class that holds those Cards that have been dealt to each player from the Deck.


# Step 2: Create a Card Class
# A Card object really only needs two attributes: suit and rank.
# You might add an attribute for "value" - we chose to handle value later when developing our Hand class.
# In addition to the Card's __init__ method, consider adding a __str__ method that,
# when asked to print a Card, returns a string in the form "Two of Hearts"

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


# c = Card("Hearts", "Two")
# print(c)


# Step 3: Create a Deck Class
# Here we might store 52 card objects in a list that can later be shuffled.
# First, though, we need to instantiate all 52 unique card objects and add them to our list.
# So long as the Card class definition appears in our code, we can build Card objects inside our Deck __init__ method.
# Consider iterating over sequences of suits and ranks to build out each card. This might appear inside a Deck class __init__ method:
#
# for suit in suits:
#     for rank in ranks:
#
# In addition to an __init__ method we'll want to add methods to shuffle our deck, and to deal out cards during gameplay.
#
# OPTIONAL: We may never need to print the contents of the deck during gameplay,
# but having the ability to see the cards inside it may help troubleshoot any problems that occur during development.
# With this in mind, consider adding a __str__ method to the class definition.


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        str = ''
        for card in self.deck:
            str += '\n' + card.__str__()
        return str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# test_deck = Deck()
# print(test_deck)


# Step 4: Create a Hand Class
# In addition to holding Card objects dealt from the Deck,
# the Hand class may be used to calculate the value of those cards using
# the values dictionary defined above.
# It may also need to adjust for the value of Aces when appropriate.

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Step 5: Create a Chips Class
# In addition to decks of cards and hands, we need to keep track of a Player's starting chips,
# bets, and ongoing winnings.
# This could be done using global variables, but in the spirit of object oriented programming,
# let's make a Chips class instead!

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        pass

    def lose_bet(self):
        self.total -= self.bet
        pass
