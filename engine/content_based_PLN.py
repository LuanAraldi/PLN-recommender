#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd 
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import re
import dask.dataframe as dd
import json
import sys
from functools import reduce
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
warnings.filterwarnings('ignore')


# ## Lendo base de dados em CSV

# In[3]:


df = pd.read_csv('1429_1.csv')


# ### Como mostra os dados acima, existem 34660 reviews de produtos identificados, mas somente 34658 ids de produto  
# ### <span style="color:red">TRATAR ISSO</span>

# In[5]:



# ## Agrupando produtos por média de nota de review  
# Isso será usado para facilitar no cálculo da correlação de produtos mais a frente

# In[6]:


products = pd.DataFrame(df.groupby('asins')['reviews.rating'].mean())


# ## Identifica quantas avaliações existem por produto e insere no dataframe

# In[9]:


products['number_of_ratings'] = df.groupby('asins')['reviews.rating'].count()





# ## Motor de recomendação
# ### Criação de uma matriz de produtos com avaliações

# In[14]:


df.processed_categories = df.categories.apply(lambda row: row.split(','))


# In[16]:


df = df[['name', 'asins', 'brand', 'categories', 'manufacturer', 'reviews.title', 'reviews.text']]
#df = df.drop_duplicates(subset=['asins'])

df['name'] = df['name'].map(lambda x: re.split(', | \s | \n', str(x).lower()))
df['categories'] = df['categories'].map(lambda x: re.split(', | \&', str(x).lower()))
df.set_index('asins', inplace=True)



# In[41]:


def get_sentiment_score(review):
    client = language.LanguageServiceClient()
    document = types.Document(content=review.get('reviews.text', ''), type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client.analyze_entity_sentiment(document=document)
    review['parsed_text'] = [entity.name for entity in sentiment_score.entities if entity.sentiment.score > 0 or not entity.sentiment.score] 
    return review


# In[20]:


#get_ipython().run_line_magic('env', 'GOOGLE_APPLICATION_CREDENTIALS=/home/luan/tcc/creds/TTC-PLN-edde7bd554e0.json')


# In[21]:


#df['reviews.text'].apply(lambda row: get_sentiment_score(str(row)))
dict_dataframe = df.to_dict('records')


# In[50]:


pool = ThreadPoolExecutor(4)
#parsed_text_file = open('./parsed_text_file.json', 'w+')
count = 0
success = 0
total = len(dict_dataframe)

new_structure = []

for item in pool.map(get_sentiment_score, dict_dataframe):
    pool.shutdown(True)
    count += 1
    if item:
        success += 1
        #parsed_text_file.write(json.dumps(item)+'\n')
        new_structure.append(item)

    print('{}/{}({})'.format(success, count, total))

#parsed_text_file.close()

