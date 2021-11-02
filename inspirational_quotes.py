from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

bot=ChatBot('Inspiration Quotes')
bot.set_trainer(ListTrainer)
df=pd.read_csv('quotes_data.csv',encoding ='latin1')
new = df["hrefs"].str.split("src=t_", n = 1, expand = True)
df['quotes_type']=new[1]
author = df["lines"].str.split(".-", n = 1, expand = True)
df["quotes_lines"]=author[0]
dataset=df.drop(['lines', 'hrefs'], axis=1)
df_new = dataset.groupby('quotes_type').agg({'quotes_lines': ', '.join}).reset_index()
final_df=df_new[['quotes_type','quotes_lines']]
question=list(final_df['quotes_type'])
for index, row in final_df.iterrows():
    ques=row['quotes_type']
    ans=row['quotes_lines']
    bot.train([ques, ans])

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
