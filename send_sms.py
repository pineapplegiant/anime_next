#import APP_SETTINGS
import os                                          # Access to Environment Variables
from twilio.rest import Client                     # Client object from Twilio

account_sid = "TWILIO_ACCOUNT_SID" # Twilio stuff
auth_token =  "TWILIO_AUTH_TOKEN"  # Twilio stuff

my_number = "MY_PHONE_NUMBER"
twilio_number = "TWILIO_PHONE_NUMBER"

message_send = "Hello, world!"

client = Client(account_sid, auth_token)           # Create Twilio Rest client object

client.messages.create(
    to= my_number,
    from_= twilio_number,
    body= message_send
)
