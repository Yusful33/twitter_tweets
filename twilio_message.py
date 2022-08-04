import os
from twilio.rest import Client
from gather_tweets_utils import FROM_NUMBER, TO_NUMBER, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, STATUS_CALLBACK


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# client = Client(account_sid, auth_token)
# message = client.messages \
#         .create(
#             body='Article: https://t.co/aCJh9xr3UA',
#             from_='123-345-5667',
#             to='123-345-5668',
#         )


class TwilioClient():
    def __init__(self, from_number, to_number):
        self._account_sid = os.environ[TWILIO_ACCOUNT_SID]
        self._auth_token = os.environ[TWILIO_AUTH_TOKEN]
        self.status_callback = STATUS_CALLBACK
        self.from_number = FROM_NUMBER
        self.to_number =  TO_NUMBER 
        self._client = Client(self._account_sid, self._auth_token)

    def send_message(self, message_text):
        """Sends a text message using twilio client."""
        message = self._client.messages \
        .create(
            body=message_text,
            from_=self.from_number,
            status_callback = self.status_callback,
            to=self.to_number
        )
# client = TwilioClient(FROM_NUMBER,TO_NUMBER)
# client.send_message('Article:')