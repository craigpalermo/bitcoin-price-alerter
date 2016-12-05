from clients.coinbase import get_bitcoin_sell_price
from clients.twilio import send_sms


class PriceAlerter(object):
    def __init__(self, recipient, min_limit, max_limit):
        self.recipient = recipient
        self.min_limit = min_limit
        self.max_limit = max_limit

    def poll(self):
        """
        Gets the current Bitcoin sell price from Coinbase, then sends an SMS text message using
        Twilio if the price is outside the given bounds.
        :return:
        """
        amount, currency = get_bitcoin_sell_price()

        if not self.min_limit <= amount <= self.max_limit:
            message = "Alert: Current price of 1 BTC is {:.2f} {}".format(amount, currency)
            send_sms(self.recipient, message)
            print(message)
        else:
            print("Current price of 1 BTC is {:.2f} {}. Within bounds, doing nothing.".format(amount, currency))
