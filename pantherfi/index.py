from flask import Flask, jsonify, request
import pymongo
import json

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

node = db["node"]
observations = db["observations"]



@app.route('/')
def get_observations():
  obs = node["observations"]
  if(len(obs) < 1440):  #assuming updates by the minute
  	return jsonify(obs)
  else:
  	return jsonify(obs[len(obs) - 14401,len(obs) -1]):
  


@app.route('/', methods=['POST'])
def add_observation():
  iden = observations.insert_one(request.get_json())
  
  node["observations"].append(iden)
  return '', 204
