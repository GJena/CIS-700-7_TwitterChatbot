import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
# import translate

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def launch_alexa():
    welcome_msg = 'welcome to twitter bot.'
    return statement(welcome_msg)

@ask.intent("ChatIntent", convert = {"Text" : str})
def chat_alexa(Text):
	return statement(Text)
    


if __name__ == '__main__':
    app.run(debug=True)
