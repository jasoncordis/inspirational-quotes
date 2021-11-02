from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Saul Goodman')
trainer = ListTrainer(bot)
trainer.train([
    "Saul Goodman is… He’s the last line of defense for the little guy. Are you getting sold down the river? He’s a life raft. You getting stepped on, he’s a sharp stick. You got Goliath on your back, Saul’s the guy with the slingshot. He’s a righter of wrongs. He’s friend to the friendless. That’s Saul Goodman."
    "You know why God made snakes before he made lawyers? He needed the practice.",
])

trainer.train([
    "Only two things I know about Albuquerque. Bugs Bunny should’ve taken a left turn there. And, give me a hundred tries, I’ll never be able to spell it.",
    "My real name’s McGill. The Jew thing I just do for the homeboys. They all want a pipe-hitting member of the tribe, so to speak…",
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText=userText.lower()
    if (userText=="hello" or userText=="Hello"):
        str_question=','.join(question)
        sentence = "S'all good, man."
    else:
         data= str(bot.get_response(userText))
         sentence = data.replace(", ", ".\n")
    return  sentence

if __name__ == "__main__":
    app.run()
