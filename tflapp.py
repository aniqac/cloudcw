from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import requests
import  requests_cache

requests_cache.install_cache('tfl_api_cache', backend='sqlite', expire_after=36000)

app = Flask(__name__)

air_url = 'https://api.tfl.gov.uk/AirQuality'


@app.route('/airquality',  methods=['GET'])
def airband():

    resp = requests.get(air_url)
    if resp.ok:
        air = resp.json()
    else:
        print(resp.reason)

    air= {air["url"]:air["name"] for air in air_json}

    air_quality_band = dict.fromkeys(air.keys(), 0)

    air_quality_band.pop("all-air")


    for air in airs:
        air_quality_bandair["air"] += 1


    air_outcome_band = {'None': 0}
    for air in airs:
        outcome = acc["outcome_status"]
        if not outcome:
            air_outcome_stats['None'] += 1
        elif outcome['air'] not in acc_outcome_band.keys():
            air_outcome_band.update({outcome['air']:1})
        else:
            air_outcome_stats[outcome['air']] += 1


if __name__=="__main__":
    app.run(port=8080, debug=True)
