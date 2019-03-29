#!/usr/bin/env python
# coding: utf-8

# ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
# http://gushwell.ldblog.jp/archives/52525991.html

# In[1]:


import pymongo
from flask import Flask, render_template, request


# In[2]:


class SearchInfo:
    def __init__(self, name, area, tag):
        self.name = name
        self.area = area
        self.tag = tag


# In[3]:


class Searcher:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['test_database']
        self.co = self.db.artist
 
    def search(self, info):
        query = { '$and' : [ ]}
        if info.name != '':
            cond = []
            cond.append({ 'aliases.name': info.name })
            cond.append({ 'name': info.name })
            query['$and'].append({ '$or': cond })
        if info.area != '':
            query['$and'].append({ 'area': info.area })
        if info.tag != '':
            query['$and'].append({ 'tags.value': info.tag })
        q2 = self.co.find(query).sort('rating.count', pymongo.DESCENDING)
        return list(q2)[:100]


# In[4]:


app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        searcher = Searcher()
        results = searcher.search(SearchInfo(request.form['name'], request.form['area'], request.form['tag']))
        return render_template('result.html', artists=results) 
    else:
        return render_template('search.html') 
 
if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




