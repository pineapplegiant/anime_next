# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from test import soup_it_up

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    response_anime = soup_it_up()
    # Add a message
    resp.message(response_anime)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
