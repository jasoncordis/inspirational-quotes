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
bot.train(["How is Howard?", "Howard is a teensy, tiny man in a teensy-weensy little bubble.  You know why I didn't take his job? Because it was too small! I don't care about it! I was nothing to me! I was a bacterium! I travel in worlds he can't even imagine! He can't conceive of what I'm capable of! I'm so far beyond him! I'm like a god in human clothing! Lighting bolts shoot from my fingertips!"])
bot.train(["What's your opinion on this politician?", "Some people are immune to good advice."])
bot.train(["Tell me a joke.", "Why do they bury lawyers under 20 feet of dirt? Because deep down, they’re really good people."])
bot.train(["Tell me a joke.", "Why do they bury lawyers under 20 feet of dirt? Because deep down, they’re really good people."])
bot.train(["Tell me a joke.", "Why do they bury lawyers under 20 feet of dirt? Because deep down, they’re really good people."])
bot.train(["Tell me a joke.", "Why do they bury lawyers under 20 feet of dirt? Because deep down, they’re really good people."])

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
