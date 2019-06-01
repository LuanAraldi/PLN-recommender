#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["MONGO_URI"] = "mongodb://luan:luan1996@ds231307.mlab.com:31307/heroku_8ct6fzlj"

mongo = PyMongo(app)

def recommendations(pid, cosine_sim, indices, df):
    
    recommended_prds = []
    
    idx = indices[indices == pid].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_5 = list(score_series.iloc[0:5].index)
    
    for i in top_5:
        recommended_prds.append(list(df.index)[i])
        
    return recommended_prds

def get_product(id):
    product = mongo.db.products.find_one({"id": id})
    return {'id': product['id'], 'name': product['name'], 'price': product['price'], 'image':product['image']}

@app.route('/rec/pln/<path:id>', methods=['GET'])
@cross_origin()
def rec_pln(id):
    cosine = np.load('cosine_sim_pln.npy')
    indices = pd.read_pickle('indices_pln.pkl')
    df = pd.read_pickle('df_pln.pkl')
    
    recs = recommendations(id, cosine, indices, df)
    parsed_recs = [get_product(str(rec)) for rec in recs]
    
    return jsonify({'recs': parsed_recs})

@app.route('/rec/original/<path:id>', methods=['GET'])
@cross_origin()
def rec_original(id):
    cosine = np.load('cosine_sim.npy')
    indices = pd.read_pickle('indices.pkl')
    df = pd.read_pickle('df.pkl')

    recs = recommendations(id, cosine, indices, df)
    parsed_recs = [get_product(str(rec)) for rec in recs]
    
    return jsonify({'recs': parsed_recs})

@app.route('/event', methods=['POST'])
@cross_origin()
def receive_event():
    doc = mongo.db.event.insert(request.json)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))