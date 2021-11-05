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
bot.train(["How is Chuck?", "My brother... my brother was sick. And he's alone. I spent years caring for him, and he hated me. The only family I had left and he hated me. He hated my guts."])
bot.train(["Who is Chuck?", "My brother... my brother was sick. And he's alone. I spent years caring for him, and he hated me. The only family I had left and he hated me. He hated my guts."])
bot.train(["How is Kim?", "How do you know Kim? Did Lalo send you? Don Lalo?"])
bot.train(["Who is Hector?", "Tio Salamanca. Old guy in a wheelchair. Um, doesn't talk. Rings a bell. I don't mean 'Does that ring a bell?' I mean the guy actually has to ring a bell."])
bot.train(["I am a kid", "I loved school when I was that age. See-saws, story time, chasing girls with sticks."])
bot.train(["Do you know chemistry?", "Heh-heh...I was terrible at chemistry. I'm more of a humanities guy."])
bot.train(["How do I get my case to be perfect?", "Perfection is the enemy of perfectly adequate."])
bot.train(["Where did you go to Law School?", "My diploma says the University of American Samoa Law School, and that's exactly what it sounds like - that's a correspondence school. I wish it said Georgetown, heh, or Northwestern... but UAS was the only one that would take me. 'Cause let me tell ya, I wasn't a natural."])
bot.train(["Why do I need to hire a lawyer?", "Lawyers – you know, we’re like health insurance. You hope you never need it. But, man oh man, not having it – no."])
bot.train(["Tell me a joke.", "What’s the difference between a vacuum cleaner and a lawyer on a motorcycle? The vacuum cleaner has the dirt bag on the inside."])

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
