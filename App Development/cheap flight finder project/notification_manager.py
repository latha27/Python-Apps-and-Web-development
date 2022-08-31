from twilio.rest import Client

account_sid = "ACb55e64befd991304125b5fb64fa46175"
auth_token = "6d5eaf0f2df5cdf443288f1d8b25344a"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+19805258168',
            to='+32467606413'
        )
        # Prints if successfully sent.
        print(message.sid)
    #This class is responsible for sending notifications with the deal flight details.
