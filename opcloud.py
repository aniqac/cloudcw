from flask import Flask, render_template, request, jsonify
import json
import requests


app = Flask(__name__)

url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_callingcode = 'https://restcountries.eu/rest/v2/callingcode/{callingcode}'
url_city = 'https://restcountries.eu/rest/v2/capital/{capital}'

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'user' or request.form['password'] != 'user':
			error = 'The credentials entered are incorrect!'
		else:
			return render_template('homepage.html')
	return render_template('loginpage.html', error=error)

@app.route('/homepage',  methods=['GET', 'POST'])
def home():
	return render_template('homepage.html')

@app.route('/name',  methods=['GET', 'POST'])
def name_country():
    url = url_name.format(name=request.form.get('name'))
    response = requests.get(url)
    if response.status_code == 404:
        return "<h1>Error, page does not exist!</h1>", 404
    response = response.json()
    return render_template('backg.html', result = response)

@app.route('/callingcode',  methods=['GET', 'POST'])
def callcode():
    url = url_callingcode.format(callingcode=request.form.get('callingcode'))
    response = requests.get(url)
    if response.status_code == 404:
        return "<h1>Error, page does not exist!</h1>", 404
    response = response.json()
    return render_template('backg.html', result = response, par="Code {}".format(request.form.get('callingcode')))

@app.route('/city',  methods=['GET', 'POST'])
def capcity():
	url = url_city.format(capital=request.form.get('city'))
	response = requests.get(url)
	if response.status_code == 404:
		return "<h1>Error, page does not exist!</h1>", 404
	response = response.json()
	return render_template('backg.html', result = response, par="cityname {}".format(request.form.get('city')))



if __name__=="__main__":
    app.run(port=8080, debug=True)
