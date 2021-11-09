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
    database_uri='mongodb+srv://user:csc675@cluster0.7udau.mongodb.net/libraryapp?retryWrites=true&w=majority',
    tie_breaking_method="random_response")

bot.set_trainer(ListTrainer)
bot.train(["Tell me a joke.", "How many lawyers does it take to change a light bulb? Three... one to climb the ladder, one to shake it, and one to sue the ladder company."])
bot.train(["Tell me a joke.", "Um, what do lawyers and sperm have in common? Oh, just... Um. 3 million... No, wait. Um, 1 in 3 million... have a chance of becoming a human being."])
bot.train(["Tell me a joke.", "Why do they bury lawyers under 20 feet of dirt? Because deep down, they’re really good people."])
bot.train(["Tell me a joke.", "What’s the difference between a tick and a lawyer? The tick falls off when you’re dead!"])
bot.train(["Tell me a joke.", 'What do you call a lawyer with an IQ of 60? "Your Honor."'])
bot.train(["Tell me a joke.", "What do you get when you cross the Godfather with a lawyer? An offer you can’t understand."])


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
