from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Inspiration Quotes', 
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database2.sqlite3')
bot.set_trainer(ListTrainer)
bot.train(["Tell me a joke.", "You know why God made snakes before he made lawyers? He needed the practice."])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText=userText.lower()
    data= str(bot.get_response(userText))
    return data

if __name__ == "__main__":
    app.run()
