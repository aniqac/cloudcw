

# Country Info
> This application allows you to search a country, language, and currency. It then shows you which country for example speaks that language or uses the currency it will also show the corresponding region. The external IP is 34.65.42.244 
>
## API Used
```python
url_countries = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_currency = 'https://restcountries.eu/rest/v2/currency/{currency}'
url_lang = 'https://restcountries.eu/rest/v2/lang/{et}'
```


## Process
	Open the command line and direct to where the app is
	Next create a virtual environment:

	python3 -m venv name_of_project
	source name_of_project/bin/activate

	You then need to activate the virtual environment using this command:
	source name_of_project/bin/activate

	From app directory run this:
	python -m pip install -U -r requirements.txt

	To run the app use the following command:
	python cloud.py

	If there are no errors then a link will appear on the terminal, clicking on this   will then take you to the the website:

	 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 151-572-586

	 Set region and zone set for the new cluster:
	 gcloud config set compute/zone europe-west2-b 
	 export PROJECT_ID="$(gcloud config get-value project -q)
	 
	 The next section was all done on google cloud shell.
	 Cassandra in Kubernetes section was done by using this command:
	 gcloud container clusters create cassandra --num-nodes=3 --
	 machine-type "n1-standard-2" 		  		
	 
	 The following had to be downloaded using this command:
	 wget -O cassandra-peer-service.yml http://tinyurl.com/yyxnephy 
	 wget -O cassandra-service.yml http://tinyurl.com/y65czz8e
	 wget -O cassandra-replication-controller.yml http://tinyurl.com/y2crfsl8
	
	 Then run the downloads using these commands:
	 kubectl create -f cassandra-peer-service.yml 
	 kubectl create -f cassandra-service.yml 
	 kubectl create -f cassandra-replication-controller.yml

	 This was then entered, which gave us the name of our cassandra container:
	 kubectl get pods -l name=cassandra
	 
	Check that the ring has been formed between all of the  Cassandra instances:
	kubectl exec -it cassandra-h46t5 -- nodetool status
	
	Using the same container, copied my data from the previous section: 
	kubectl cp data.csv cassandra-h46t5:/data.csv 
	
	run cqlsh inside the container: 
	kubectl exec -it cassandra-h46t5 cqlsh 
	
	built my keyspace: 
	CREATE KEYSPACE data WITH REPLICATION {'class' : 'SimpleStrategy', 'replication_factor' : 2};
	
	Created the table for my stats and ingest the CSV via copy:
	CREATE TABLE data.stats (Name text PRIMARY KEY, language text, ) ;
	COPY data.stats(Name,language) FROM 'data.csv' WITH DELIMITER=',' AND HEADER=TRUE;
	
	Used this to build the image:
	docker build -t gcr.io/${PROJECT_ID}/data-app:v1 .

	Pushed it to Google Resporitory:
	docker push gcr.io/${PROJECT_ID}/data-app:v1
	
	Then run:
	kubectl run data-app --image=gcr.io/${PROJECT_ID}/data-app:v1 --port 8080
	kubectl expose deployment data-app --type=LoadBalancer --port 80 --target-port 8080

	Command to get the external IP is kubectl get services this shows the data-app IP to be:
	34.65.42.244 
```
	This is the table created can be shown when you enter the command: 
	select * from data.stats;
	

	 name                               | language
------------------------------------+----------
                            Ecuador |  Spanish
                               Peru |  Spanish
                              Spain |  Spanish
 Venezuela (Bolivarian Republic of) |  Spanish
                            Uruguay |  Spanish
                          Nicaragua |  Spanish
                           Paraguay |  Spanish
                          Guatemala |  Spanish
                        El Salvador |  Spanish
                           Holy See |  Italian
                         San Marino |  Italian
                  Equatorial Guinea |  Spanish
                           Colombia |  Spanish
                               Guam |  Spanish
                 Dominican Republic |  Spanish
                              Chile |  Spanish
                         Costa Rica |  Spanish
                        Switzerland |  Italian
                        Puerto Rico |  Spanish
                               Fiji |    Hindi
                              India |    Hindi
                           Honduras |  Spanish
                               Cuba |  Spanish
                             Mexico |  Spanish
                     Western Sahara |  Spanish
                             Belize |  Spanish
                          Argentina |  Spanish
                             Panama |  Spanish
                              Italy |  Italian
   Bolivia (Plurinational State of) |  Spanish
   
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


```
