"""My flask app."""

import pandas as pd
import markovify
from flask import Flask
app = Flask(__name__)

beer_descs = pd.read_csv('beer_descs.csv', index_col=False)
beer_desc_model = markovify.Text(beer_descs.text)

@app.route('/')
def generate_beer_desc():
    return beer_desc_model.make_sentance()
