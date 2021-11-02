from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Inspiration Quotes')
trainer = ListTrainer(bot)

trainer.train([
    "Hello"
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText=userText.lower()
    data= str(bot.get_response(userText))
    sentence = data.replace(", ", ".\n")
    return sentence

if __name__ == "__main__":
    app.run()
