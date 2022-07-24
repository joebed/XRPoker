from models.card import Card, Suit, Rank
from models.player import Player

class Deck:
    def __init__(self): 

        # Initialize deck
        self.deck = []
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(Rank(j), Suit(i)))


    def shuffle(self):
        pass
    
    def dealTopCard(self) -> Card:
        return self.deck.pop(0)

        