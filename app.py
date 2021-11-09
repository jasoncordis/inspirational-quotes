from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.storage import StorageAdapter
from chatterbot.response_selection import get_random_response
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Saul Goodman',     storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    response_selection_method=get_random_response,
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb+srv://user:csc675@cluster0.7udau.mongodb.net/libraryapp?retryWrites=true&w=majority',
    )

bot.set_trainer(ListTrainer)
bot.train(["Can you describe your dad?", "Everybody liked my dad because he was a soft touch. Every deadbeat in the neighborhood owed him money. You come in here with a sob story and you leave with a pat on the back and a gallon of milk. He could have made it work, he could have sold beer and cigarettes to the kids from Mary Margaret's, but no. Not him. He was never gonna do what he had to do."])

bot.set_trainer(ListTrainer)

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
