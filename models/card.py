from dataclasses import dataclass
from enum import Enum

class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

class Rank(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

@dataclass
class Card:
    rank: Rank 
    suit: Suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"