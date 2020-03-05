

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC22d6dd091abf92fb4d9c117975c82f0d'
auth_token = '63559d6ac24ec5827b601621417b6891'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="오레, 이거 테스트",
                     from_='+14159650576',
                     to='+821025889120'
                 )

print(message.sid)