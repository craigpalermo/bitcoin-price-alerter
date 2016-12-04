#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
from price_alerter import PriceAlerter
from clients import coinbase as coinbase_client

import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Send an SMS text message when Bitcoin reaches a certain value')
parser.add_argument('--max', dest='max_limit', nargs=1, help='Alert when price is GREATER THAN max')
parser.add_argument('--min', dest='min_limit', nargs=1, help='Alert when price is LESS THAN max')
parser.add_argument('--phone', dest='recipient_phone', nargs=1, help='Recipient phone number for SMS alerts')
parser.add_argument('--test', action='store_true')


def main():
    args = parser.parse_args()
    min_limit, max_limit = args.min_limit, args.max_limit

    if min is not None or max is not None:
        min_limit = float(min_limit[0]) if min_limit is not None else 0
        max_limit = float(max_limit[0]) if max_limit is not None else float("inf")

        if max_limit <= min_limit:
            print("Max must be greater than min limit. Exiting.")
            return
        elif not args.recipient_phone and not args.test:
            print("No recipient phone number given. Exiting.")
            return
        elif args.test:
            coinbase_client.test()
            return

        recipient_phone = args.recipient_phone[0]
        alerter = PriceAlerter(recipient_phone, min_limit, max_limit)
        print("Bitcoin price alert now running. Min: {:.2f}, Max: {:.2f}".format(min_limit, max_limit))

        # Display current sell price
        current_sell_price, currency = coinbase_client.get_bitcoin_sell_price()
        print("Current BTC sell price: {:.2f} {}".format(current_sell_price, currency))

        # Create blocking scheduler to run on interval
        try:
            scheduler = BlockingScheduler()
            scheduler.add_job(lambda: alerter.poll(), 'interval', minutes=10)
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
    else:
        print("No price limits given. Exiting.")

if __name__ == "__main__":
    main()
