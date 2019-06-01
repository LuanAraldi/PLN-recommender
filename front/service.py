from flask import Flask
app = Flask(__name__)

def recommendations(pid, cosine_sim = cosine_sim):
    recommended_prds = []
    
    idx = indices[indices == pid].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_5 = list(score_series.iloc[1:6].index)
    
    for i in top_5:
        recommended_prds.append(list(df_parsed.index)[i])
        
    return recommended_prds

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
app.run()
