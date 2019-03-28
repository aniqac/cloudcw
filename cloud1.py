from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import requests
import requests_cache


app = Flask(__name__)
CORS(app)
url_countries = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_currency = 'https://restcountries.eu/rest/v2/currency/{currency}'
url_lang = 'https://restcountries.eu/rest/v2/lang/{et}'

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'The credentials are incorrect!'
		else:
			return render_template('login.html', error=error)


@app.route('/',  methods=['GET'])
def whatever_home():
	return "This is my page on different countries"

@app.route('/all',  methods=['GET'])
def all_countries():
    response = requests.get(url_countries).json()
    dict_test = {'List of Countries': []}
    for a in response:
        dict_test['List of Countries'].append(a['name'])
    # return render_template('list.html', result = response)
    return jsonify(dict_test)

@app.route('/name/<countryinput>',  methods=['GET'])
def name_country(countryinput):
    url = url_name.format(name=countryinput)
    response = requests.get(url)
    dict_test = {'Country Name': []}
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()
    for a in response:
        dict_test['Country Name'].append(a['name'])
    #return render_template('background.html', result = response)
    return jsonify(dict_test)

@app.route('/currency/<currencyinput>',  methods=['GET'])
def currency (currencyinput):
    url = url_currency.format(currency=currencyinput)
    response = requests.get(url)
    dict_test = {'Currency List': []}
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()
    for a in response:
        dict_test['Currency List'].append(a['name'])
    #return render_template('background1.html', result = response)
    return jsonify(dict_test)

@app.route('/lang/<langinput>',  methods=['GET'])
def language (langinput):
	url = url_lang.format(et=langinput)
	response = requests.get(url)
	dict_test = {'Language List': []}
	if response.status_code == 404:
		return "<h2>Error, page does not exist!</h2>", 404
	response = response.json()
	for a in response:
		dict_test['Langauge List'].append(a['name'])
	#return render_template('background2.html', result = response)
    return jsonify(dict_test)


if __name__=="__main__":
    app.run(port=8080, debug=True)
