from flask import Flask, jsonify, request
import pymongo
import json

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

nodes = db["nodes"]
observations = db["observations"]



@app.route('/')
def get_observations():
  obs = observations.find({}) # get all observations - query to only get last 24h will be written later
  return jsonify(obs)
  


@app.route('/', methods=['POST'])
def add_observation():
  obs_data = request.get_json()
  # todo: validate obs
  matched_node = nodes.find_one({"hostname": obs_data["hostname"]}) # find the right node by hostname
  obs_data["node"] = matched_node["_id"] # add ref
  iden = observations.insert_one(obs_data) # insert the observation
  return '', 204
