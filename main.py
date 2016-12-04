#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
from price_alerter import PriceAlerter

import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Send an SMS text message when Bitcoin reaches a certain value')
parser.add_argument('--max', dest='max_limit', nargs=1, help='Alert when price is GREATER THAN max')
parser.add_argument('--min', dest='min_limit', nargs=1, help='Alert when price is LESS THAN max')
parser.add_argument('--phone', dest='recipient_phone', nargs=1, help='Recipient phone number for SMS alerts',
                    required=True)


def main():
    args = parser.parse_args()
    min_limit, max_limit = args.min_limit, args.max_limit

    if min is not None or max is not None:
        min_limit = float(min_limit[0]) if min_limit is not None else 0
        max_limit = float(max_limit[0]) if max_limit is not None else float("inf")
        alerter = PriceAlerter(args.recipient_phone, min_limit, max_limit)
        print("Bitcoin price alert now running. Min: {:.2f}, Max: {:.2f}".format(min_limit, max_limit))

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
