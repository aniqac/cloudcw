from flask import Flask, jsonify, json, request
import json

with open('records.json') as f:
    all_records = json.load(f)

app = Flask(__name__)

@app.route('/airquality', methods=['GET'])
def get_all_records():
    return jsonify(all_records)
