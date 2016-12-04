from twilio.rest import TwilioRestClient
from settings import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_SENDER

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms(recipient, body):
    client.messages.create(
        to=recipient,
        from_=TWILIO_SENDER,
        body=body
    )
