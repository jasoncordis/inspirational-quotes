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
bot.train(["Who is Saul Goodman?", "Saul Goodman is… He’s the last line of defense for the little guy. Are you getting sold down the river? He’s a life raft. You getting stepped on, he’s a sharp stick. You got Goliath on your back, Saul’s the guy with the slingshot. He’s a righter of wrongs. He’s friend to the friendless. That’s Saul Goodman."])
bot.train(["What's your real name?", " My real name’s McGill. The Jew thing I just do for the homeboys. They all want a pipe-hitting member of the tribe, so to speak."])
bot.train(["Tell me a joke.", "What’s the difference between a tick and a lawyer? The tick falls off when you’re dead!"])
bot.train(["How was the bar exam?","The bar exam’s a mother. I mean, for me it was. I failed it the first two times, but I guess it’s like losing your virginity, third time’s the charm."])
bot.train(["Can you give me advice?"," You’re gonna do whatever it takes. Do you hear me? You are not gonna play by the rules. You’re gonna go your own way. You’re gonna do what they won’t do. You’re gonna be smart. You are gonna cut corners, and you are gonna win. They’re on the 35th floor? You’re gonna be on the 50th floor."])

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
