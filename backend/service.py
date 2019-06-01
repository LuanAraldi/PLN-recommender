from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pln"
mongo = PyMongo(app)

def recommendations(pid, cosine_sim, indices, df):
    
    recommended_prds = []
    
    idx = indices[indices == pid].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_5 = list(score_series.iloc[0:5].index)
    
    for i in top_5:
        recommended_prds.append(list(df.index)[i])
        
    return recommended_prds

@app.route('/rec/pln/<path:id>', methods=['GET'])
def rec_pln(id):
    cosine = np.load('cosine_sim_pln.npy')
    indices = pd.read_pickle('indices_pln.pkl')
    df = pd.read_pickle('df_pln.pkl')
    print(type(cosine))
    return jsonify({'recs': recommendations(id, cosine, indices, df)})

@app.route('/rec/original/<path:id>', methods=['GET'])
def rec_original(id):
    cosine = np.load('cosine_sim.npy')
    indices = pd.read_pickle('indices.pkl')
    df = pd.read_pickle('df.pkl')
    print(type(cosine))
    return jsonify({'recs': recommendations(id, cosine, indices, df)})

@app.route('/event', methods=['POST'])
def receive_event():
    doc = mongo.db.event.insert(request.json)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)