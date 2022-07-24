from models.player import Player
from models.deck import Deck

class Game:
    
    def __init__(self,
            host: Player,
            min_buyin: int,
            blind_small: int,
            blind_big: int
            ) -> None:
        self.xrp_on_table = 0
        self.host = host
        self.min_buyin = min_buyin
        self.blind_small = blind_small
        self.blind_big = blind_big
        self.players = [host]

    def __repr__(self) -> str:
        return f"***********\nGame Stats\n***********\nhost:\t{self.host.name}\nblinds:\t{self.blind_small}/{self.blind_big}\nxrp_on_table:\t{self.xrp_on_table}"

    def add_player(self, new_player: Player):
        # TODO: Check each player's address instead of just Player itself
        if new_player in self.players:
            print(f"{new_player.name} already at table")
            return
        # TODO: Don't let two people with the same name join
        self.players.append(new_player)
        print(f"{new_player.name} joined")
        

    def play_hand(self):
        __players_in_hand = []
        for player in self.players:
            player.prepare_for_hand()
            if player.in_next_hand:
                __players_in_hand.append(player)

        __deck = Deck()
        self.deal(__deck, __players_in_hand)

        
    def deal(self, deck: Deck, in_hand_players):
        deck.shuffle()
        for _ in range(2):
            for player in in_hand_players:
                new_card = deck.dealTopCard()
                player.hole_cards.append(new_card)
