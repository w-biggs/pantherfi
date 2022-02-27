from flask import Flask, Response, request
import pymongo
from bson import json_util
import time

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pantherfi"]

nodes = db["nodes"]
observations = db["observations"]



@app.route('/')
def get_observations():
  obs = observations.find({}) # get all observations - query to only get last 24h will be written later
  return Response(
    json_util.dumps(obs),
    headers={"Access-Control-Allow-Origin":"*"},
    mimetype='application/json'
  )
  


@app.route('/', methods=['POST'])
def add_observation():
  print('received obs')
  obs_data = request.get_json()
  print(obs_data)
  # todo: validate obs
  matched_node = nodes.find_one({"hostname": obs_data["hostname"]}) # find the right node by hostname
  print(matched_node)
  obs_data["node"] = matched_node["_id"] # add ref
  obs_data["timestamp"] = int(time.time()) # add timestamp
  iden = observations.insert_one(obs_data) # insert the observation
  print('inserted obs')
  return '', 204
