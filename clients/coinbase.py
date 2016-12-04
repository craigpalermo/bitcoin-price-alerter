from coinbase.wallet.client import Client
from settings import COINBASE_API_KEY, COINBASE_API_SECRET

client = Client(COINBASE_API_KEY, COINBASE_API_SECRET)


def _get_sell_price():
    return client.get_sell_price(currency_pair='BTC-USD')


def get_bitcoin_sell_price():
    response = _get_sell_price()
    return float(response["amount"]), response["currency"]


def test():
    message = "Testing connection to Coinbase API: "

    try:
        response = _get_sell_price()

        if "amount" in response and "errors" not in response:
            status = "success"
        else:
            status = "failure"
    except Exception:
        status = "failure"

    print("".join([message, status.upper()]))
