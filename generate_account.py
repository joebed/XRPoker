from xrpl.clients.json_rpc_client import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet

# TODO: export a list of 11 accounts to a csv, automatically update this list when testnet wipes

# This is very small example in order for early testing, annoying to use
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

test_wallet = generate_faucet_wallet(client, debug=True)
print(test_wallet)