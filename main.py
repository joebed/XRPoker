from models.deck import Deck
from xrpl.clients.json_rpc_client import JsonRpcClient
from models.game import Game

from models.player import Player
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

deck = Deck()

dylan = Player(address="r4DWggWeJsDmkNmX8xSQyZnP6pfWsk4qvi", name="Dylan")
boesch = Player(address="r4CjZNxsrRi1bxAjCBh3CouzRQXKdGVLJo", name="BOESCH")
dom = Player(address="rKf26GQfrvYzWHrRnX6qwPDLRd1PXh9QUm", name="Dom")
game = Game(dylan, 200, 1, 2)
game.add_player(boesch)
game.add_player(dom)

game.play_hand()


