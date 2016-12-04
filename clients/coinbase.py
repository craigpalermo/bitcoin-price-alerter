from coinbase.wallet.client import Client
from settings import COINBASE_API_KEY, COINBASE_API_SECRET

client = Client(COINBASE_API_KEY, COINBASE_API_SECRET)


def get_bitcoin_sell_price():
    response = client.get_sell_price(currency_pair='BTC-USD')
    return float(response["amount"]), response["currency"]
