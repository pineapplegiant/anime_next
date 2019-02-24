# FLASK TWILIO "Anime Next"

## tl;dr

This app runs a flask server that will allow texts to be sent to TWILIO.
Then it will trigger a web scrape and return an anime selection for you to watch.


## Technologies:

* Flask
* Twilio
* Web scraping in python
* Ngrok for debugging

## Installation

1. Python3 
2. Create virtualenv -> `pip install virtual env` 
    * `source myproject/bin/activate`
3. Pip install requirements
    * `pip install -r requirements.txt`
4. Create your Twilio settings in a `config.py`
5. Run `export APP_SETTINGS=./config.py` in terminal

[Read this link to learn about FLASK CONFIG](http://flask.pocoo.org/docs/1.0/config/)
