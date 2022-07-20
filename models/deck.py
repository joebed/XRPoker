from card import Card, Suit, Rank
from player import Player

class Deck:
    def __init__(self): 

        # Initialize deck
        self.deck = []
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(Suit(i), Rank(j)))


    def shuffle(self):
        pass
    
    def dealTopCard(self) -> Card:
        return self.deck.pop(0)

        