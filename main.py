"""Web application that generates fake beer descriptions using markovify"""
#import pandas as pd
import markovify
from flask import Flask
app = Flask(__name__)

#beer_descs = pd.read_csv('beer_descs.csv', index_col=False)
with open('beer_desc_model.json', 'r') as f:
    model_json = f.read()
beer_desc_model = markovify.Text.from_json(model_json)

@app.route('/')
def generate_beer_desc():
    return beer_desc_model.make_sentence()
