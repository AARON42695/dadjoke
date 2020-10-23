from flask import Flask, render_template
import requests
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import string
from collections import Counter

app = Flask(__name__)

@app.route('/')
def show_table():
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept':'text/plain'}

    punc = string.punctuation
    counter = Counter()

    #fetch 10 jokes
    for i in range(10):
        response = requests.get('https://icanhazdadjoke.com/', headers=headers)
        text = response.content.decode('utf-8')
        token_list = [token.lower() for token in word_tokenize(text) if token not in punc]
        counter.update(token_list)

    df = pd.DataFrame.from_dict(counter.items())
    df.columns = ['Term', 'Count']
    top10 = df.sort_values('Count', ascending=False).head(10)
    top10['Rank'] = np.arange(1, len(top10) + 1)
    top10 = top10[['Rank', 'Term', 'Count']]
    return render_template('table.html', table=top10.to_html(classes='top10', index=False))

if __name__ == "__main__":
    app.run(debug=True)