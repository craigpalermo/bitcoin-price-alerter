# Bitcoin Price Alerter

This is a daemon that will send an SMS text message when the sell price
of Bitcoin goes above or below the given limits.

## Setup
Be sure to install packages defined in `requirements.txt` before
running.

The following environment variables must also be set using your personal
Coinbaseand Twilio API credentials.

- COINBASE_API_KEY
- COINBASE_API_SECRET
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_SENDER

## Usage
To start the daemon:

`python main.py --phone <recipient_phone> --min <lower_bound> --max
    <upper_bound>`

- `recipient_phone`: phone number preceded by country code, e.g.
"+11234567890"
- `min` (optional): send alert if price of Bitcoin drops below min
- `max` (optional): send alert if price of Bitcoin exceeds max

The program will check the price of Bitcoin every 10 minutes.

## TODO
- Allow settings to be provided via both environment variables and in a Python module
- Add command to test API connections to Coinbase and Twilio
- Don't continue alerting if price remains out of bounds over multiple
polls
