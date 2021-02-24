"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

Consider the following five hands dealt to two players:

Hand	Player 1	     	Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights

2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen

3	 	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds

4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
import os
from enum import Enum
from collections import defaultdict, Counter

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_FOLDER = os.path.join(CURRENT_DIR, '../', 'resources')

# Variables
input_file_name = os.path.join(RESOURCE_FOLDER + '/' + '54_poker_hands.txt')


class Suit(Enum):
    Spades = 1; Hearts = 2; Diamonds = 3; Clubs = 4


class CardValue(Enum):
    Two = 2; Three = 3; Four = 4; Five = 5; Six = 6; Seven = 7; Eight = 8; Nine = 9; Ten = 10; Jack = 11;
    Queen = 12; King = 13; Ace = 14;


class Card:
    suit: Suit
    value: CardValue

    def __init__(self, str_card):
        value = str_card[0]
        # Deal with values
        if value == 'J':   self.value = CardValue.Jack
        elif value == 'Q': self.value = CardValue.Queen
        elif value == 'K': self.value = CardValue.King
        elif value == 'A': self.value = CardValue.Ace
        elif value == 'T': self.value = CardValue.Ten
        elif int(value): self.value = CardValue(int(value))

        # Deal with Suits
        suit = str_card[1]
        if suit == 'S':   self.suit = Suit.Spades
        elif suit == 'H': self.suit = Suit.Hearts
        elif suit == 'C': self.suit = Suit.Clubs
        elif suit == 'D': self.suit = Suit.Diamonds

    def __str__(self):
        return self.value.name + " of " + self.suit.name

    def __repr__(self):
        return self.__str__()


"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""

def getHighCard(hand):
    tmp_hand = [card.value.value for card in hand]
    max_index = tmp_hand.index(max(tmp_hand))
    return hand[max_index]

def getPairs(hand):
    pair_map = Counter()
    pair_index = dict()

    for index, card in enumerate(hand):
        pair_map[card.value.name] += 1

    for key in pair_map:
        if pair_map[key] in pair_index:
            pair_index[pair_map[key]] += [key]
        else:
            pair_index[pair_map[key]] = [key]
    print(pair_index)

player1 = []
player2 = []
# Read Poker Hands File
with open(input_file_name) as poker_hands_file:
    while input_line := poker_hands_file.readline():
        mid_point = int(len(input_line)/2)

        # Load Hands from Line String
        player1 = [Card(str_card) for str_card in input_line[:mid_point].strip().split()]
        player2 = [Card(str_card) for str_card in input_line[mid_point:].strip().split()]

        # Perform Checks against the Hands
        # print(getHighCard(player1))
        print(player2)
        getPairs(player2)
        break