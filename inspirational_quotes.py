from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Inspiration Quotes')
bot.set_trainer(ListTrainer)
bot.train(["Who is Saul Goodman?", "Saul Goodman is… He’s the last line of defense for the little guy. Are you getting sold down the river? He’s a life raft. You getting stepped on, he’s a sharp stick. You got Goliath on your back, Saul’s the guy with the slingshot. He’s a righter of wrongs. He’s friend to the friendless. That’s Saul Goodman."])
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    data= str(bot.get_response(userText))
    return data

if __name__ == "__main__":
    app.run()
