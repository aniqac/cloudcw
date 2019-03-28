# Country Info
> This application allows you to search a country, language, and currency once you enter this it will also show the corresponding region.
## API Used
```python
url_countries = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_currency = 'https://restcountries.eu/rest/v2/currency/{currency}'
url_lang = 'https://restcountries.eu/rest/v2/lang/{et}'
```

## Code Explanation

```python
	# This route is the initial route that the user goes to login.
	@app.route('/', methods=['GET', 'POST'])

	#This is used to find method whether it is POST or GET
	request.method == 'POST'

	# In order to the POST data I do this
	request.form['username']

	# We take the password from the request and cross reference it with the password that we already have
    hash(request.form['password'])
	
	# The error code that appears when the page does not exist, in our example this would be the case when a invalid country is entered.
	if response.status_code == 404:

	# returns a html response
	return render_template('background.html', result = response)

	# html template for the homepage which is linked to the log in page. Use of colour has been applied. This also allows each page to show both the item search for and the corresponding region.
	<!DOCTYPE html>
	<html lang="en" dir="ltr">
	  <head>
	    <meta charset="utf-8">
	    <title>COUNTRY</title>
	  </head>
	  <form class="" action="{{url_for('home')}}" method="post">
	    <button type="submit" name="button">Home</button>
	  </form>
	  <body style ="background-color:powderblue;" >
	    <h1>List of countries based on {{par}}</h1>
	    <table>
	      <tr>
	        <th>Name of Country</th>
	        <th>Reg</th>
	      </tr>
	      {% for value in result %}
	      <tr>
	        <td>{{value.name}}</td>
	        <td>{{value.region}}</td>
	      </tr>
	      {% endfor %}
	    </table>
	  </body>
	</html>

	# This is the html template that creates the buttons for each of the variables I have such as country and currency along with the buttons to then search for these on the API.
		<!DOCTYPE html>
		<html lang="en" dir="ltr">
		  <head>
		    <meta charset="utf-8">
		    <title>my app</title>
		  </head>
		  <body>
		    <form class="" action="{{url_for('all_countries')}}" method="post">
		      <button type="submit" name="button">List</button>
		    </form>
		    <form class="" action="{{url_for('name_country')}}" method="post">
		      Search by name: <input type="text" name="name" value="">
		      <button type="submit" name="button">Enter</button>
		    </form>
		    <form class="" action="{{url_for('currency')}}" method="post">
		      Search by currency: <input type="text" name="currency" value="">
		      <button type="submit" name="button">Enter</button>
		    </form>
		    <form class="" action="{{url_for('language')}}" method="post">
		      Search by language: <input type="text" name="language" value="">
		      <button type="submit" name="button">Enter</button>
		    </form>
		  </body>
		</html>

		# The login and sign up html template
	<html>
	  <head>
	    <title>Flask Intro - Login Page</title>
	    {% if error %}
	       <p class="error"><strong>Error:</strong> {{ error}}
	    {% endif %}
	    <script>
	      function signup(){
	        window.location.href = "/signup"
	      }
	    </script>
	  </head>
	  <body style ="background-color:powderblue;" >
	      <h2>Please Login</h2>
	      <br>
	      <form action="" method="post">
	        Username:<input type ="text" placeholder="Username" name="username"><br/>
	         Password:<input type="password" placeholder="Password" name="password"><br/>
	        <button class="btn btn-default" type="submit" value="Login">Login</button>
	      </form>
	      <button class="btn btn-default" onclick="signup()"  value="Signup">Signup</button>
	   </body>
	</html>


```
