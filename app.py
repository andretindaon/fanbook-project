from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://test:sparta@ac-kfprgpg-shard-00-00.dqowppk.mongodb.net:27017,ac-kfprgpg-shard-00-01.dqowppk.mongodb.net:27017,ac-kfprgpg-shard-00-02.dqowppk.mongodb.net:27017/?ssl=true&replicaSet=atlas-tp9xrx-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')