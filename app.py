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
bot.train(["Tell me about Albuquerque.", "Only two things I know about Albuquerque. Bugs Bunny should’ve taken a left turn there. And, give me a hundred tries, I’ll never be able to spell it."])
bot.train(["How can I trick people?", "If you're committed enough, you can make any story work. I once told a woman I was Kevin Costner, and it worked because I believed it."])
bot.train(["Do you work with old people?", "FYI? Old people adore me."])
    
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
