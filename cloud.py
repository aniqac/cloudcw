# All the required modules 
from flask import Flask, render_template, request, jsonify
import json
import requests
from cassandra.cluster import Cluster

#Required to connect to cassandra database
cluster = Cluster(['cassandra'])
session = cluster.connect()


app = Flask(__name__)
# The list of API used
url_countries = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_currency = 'https://restcountries.eu/rest/v2/currency/{currency}'
url_lang = 'https://restcountries.eu/rest/v2/lang/{et}'

# This is the route to get to the first page that the user will come across. Has both GET and POST as it needs to be able to do both. 
# A html template is used here
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or hash(request.form['password']) != hash('admin'):
			error = 'The credentials are incorrect!'
		else:
			return render_template('home.html')
	return render_template('login.html', error=error)

# Sign up page
@app.route('/signup', methods=['GET', 'POST'])
def sign():
	error = None
	return render_template('signup.html', error=error)

# In order to get the data from the file created called "data" This is for the external IP
@app.route('/data')
def profile(name):
	rows = session.execute( """Select * From data.stats""" )
	return rows


@app.route('/home',  methods=['GET', 'POST'])
def home():
	return render_template('home.html')

#Method to specify whether it is POST or GET, leads to all countries. 
@app.route('/all',  methods=['GET', 'POST'])
def all_countries():
    response = requests.get(url_countries).json()
    dict_test = {'List of Countries': []}
    for a in response:
        dict_test['List of Countries'].append(a['name'])
    return render_template('list.html', result = response)
    #response = response.json()
	
	# A json response is available instead of using the html template
    #return jsonify(response)

@app.route('/name',  methods=['GET', 'POST'])
def name_country():
	# Gets the data from the API when user specifies country name. There are search buttons present in the templates folder which allows user to enter the data rather than having to enter it on url. This is use of forms. 
    url = url_name.format(name=request.form.get('name'))
    response = requests.get(url)
	# error code put in so that users have get feedback when incorrect information has been entered. 404 means does not exist on this page
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()

    #for a in response:
    #    dict_test['Country Name'].append(a['name'])
	#	dict_test['Reg'].append(a['region'])

    return render_template('background.html', result = response)

# To get data on currency, html template has been used for asthetics but json response also avilable. Error codes same as above
@app.route('/currency',  methods=['GET', 'POST'])
def currency():
    url = url_currency.format(currency=request.form.get('currency'))
    response = requests.get(url)
	# If error code is 404 (doesn't exists) then return the following 
    if response.status_code == 404:
        return "<h2>Error, page does not exist!</h2>", 404
    response = response.json()
    return render_template('background.html', result = response, par="Currency {}".format(request.form.get('currency')))
   # return jsonify(response)

@app.route('/lang',  methods=['GET', 'POST'])
def language():
	# This will get the requested data, in this case the language entered by the user
	url = url_lang.format(et=request.form.get('language'))
	response = requests.get(url)
	# The error code is 404, this is when the page does not exist e.g wrong spelling of language. A error message has been specified
	if response.status_code == 404:
		return "<h2>Error, page does not exist!</h2>", 404
	response = response.json()
	# A html template is available to use if needed
	#return render_template('background.html', result = response, par="Language {}".format(request.form.get('language')))
        return jsonify(response)
	
# Required to run application, host also specified and required to get external IP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
