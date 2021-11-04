from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.storage import StorageAdapter
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Saul Goodman',     storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb+srv://user:csc675@cluster0.7udau.mongodb.net/libraryapp?retryWrites=true&w=majority')
bot.set_trainer(ListTrainer)
bot.train(["This person might snitch on me and get me in trouble!", "Have you given any thought on sending him on a trip to Belize?"])
bot.train(["Should I take this opportunity?","You walk by a $20 on the sidewalk? No, you pick it up."])
bot.train(['I had a mistrial', 'Two sweetest words in the English language, "miss," "trial."'])
bot.train(['I ran out of ideas', 'There’s always another play.'])
bot.train(['I want to save my dignity, reputation, and honor', "You wanna save your dignity? You’re gonna have to fight."])
bot.train(["I'm early or late to this meeting at this time", "Never bad to be early, except in death and taxes and… some other things."])
bot.train(["I need to work on my appearance, dress nicer, stylish, and look successful.", "Got to look successful to be successful."])

           
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
