from twilio.rest import Client
import os

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
MY_NUMBER = os.environ.get('MY_NUMBER')

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_alert(self):
        message = self.client.messages.create(
            body= 'Tester',
            from_=MY_NUMBER,
            to='+14703189931'
        )
        return message.sid
