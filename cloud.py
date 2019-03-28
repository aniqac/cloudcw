from flask import Flask, render_template, request, jsonify
import json
import requests
from cassandra.cluster import Cluster

#cluster = Cluster(['cassandra'])
#session = cluster.connect()


app = Flask(__name__)

url_countries = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_currency = 'https://restcountries.eu/rest/v2/currency/{currency}'
url_lang = 'https://restcountries.eu/rest/v2/lang/{et}'

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or hash(request.form['password']) != hash('admin'):
			error = 'The credentials are incorrect!'
		else:
			return render_template('home.html')
	return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def sign():
	error = None
	return render_template('signup.html', error=error)

@app.route('/data')
def profile(name):
	rows = session.execute( """Select * From data.stats""" )
	return rows

@app.route('/home',  methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/all',  methods=['GET', 'POST'])
def all_countries():
    response = requests.get(url_countries).json()
    dict_test = {'List of Countries': []}
    for a in response:
        dict_test['List of Countries'].append(a['name'])
    return render_template('list.html', result = response)

@app.route('/name',  methods=['GET', 'POST'])
def name_country():
    url = url_name.format(name=request.form.get('name'))
    response = requests.get(url)
    #dict_test = {'Country Name': [], 'Reg': []}
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()

    #for a in response:
    #    dict_test['Country Name'].append(a['name'])
	#	dict_test['Reg'].append(a['region'])

    return render_template('background.html', result = response)

@app.route('/currency',  methods=['GET', 'POST'])
def currency():
    url = url_currency.format(currency=request.form.get('currency'))
    response = requests.get(url)
    #dict_test = {'The currency is used in the following countries': []}
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()
    #for a in response:
        #dict_test['The currency is used in the following countries'].append(a['name'])
    return render_template('background.html', result = response, par="Currency {}".format(request.form.get('currency')))

@app.route('/lang',  methods=['GET', 'POST'])
def language():
	url = url_lang.format(et=request.form.get('language'))
	response = requests.get(url)
	#dict_test = {'Here is the list of countries that speak the requested language': []}
	if response.status_code == 404:
		return "<h2>Error, page does not exist!</h2>", 404
	response = response.json()
	#for a in response:
		#dict_test['Here is the list of countries that speak the requested language'].append(a['name'])
	return render_template('background.html', result = response, par="Language {}".format(request.form.get('language')))



if __name__=="__main__":
    app.run(port=8080, debug=True)
