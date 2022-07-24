from models.card import Card

class Player:
    def __init__(self,
        address: str,
        name: str):
        self.name = name
        self.address = address
        self.stack = 0
        self.hole_cards = []
        self.in_next_hand = True

    def requestChips(self):
        pass

    def prepare_for_hand(self):
        self.hole_cards = []

    def receive_card(self, new_card: Card):
        self.hole_cards.append(Card)

    def __repr__(self) -> str:
        return f"{self.name}'s stats:\n\taddress:\t{self.address}\n\tstack:\t{self.stack}\n\thand:\t{self.hole_cards}"
