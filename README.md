# Photovoltaik

Photovoltaik is a read-only web API that provides reference data on specific energy yields of photovoltaik systems in Germany depending on their location and capacity. Thereby it enables photovoltaik operators to compare the generated energy yields with the expected yields for their PV system.

## Prerequisites
- Python3 should be installed.

## Install
Start with cloning this repository and chancge to the project directory:
```sh 
$ git clone https://github.com/clara-lupa/photovoltaik.git
$ cd photovoltaik
```
Then create a virtual environment to install the dependencies and activate this virtual envrionment:
```sh
$ python3 -m venv env  # creates virtual environment, install venv if necessary
$ source env/bin/activate
```
If you have not installed venv yet, you will be asked to install it. Follow the instructions in the terminal in order to do so, and then run the above commands again. You should see `(env)` in front of your terminals' prompt if you have activated the virtual environment successfully.

Install the depencies:
```sh
(env)$ pip install -r requirements.txt
```
Create a .env file for environment variables
```sh
(env)$ touch .env
```
In the .env file, you need to define and export your secret secret key and set the value for debug. This is done by adding the following lines to the .env file:
```
export SECRET_KEY="<your own secret key>"
export DEBUG_VALUE="True"
```
You can generate a secret key for example by using the python3 interpreter, running the command `secrets.token_hex(24)`.
The next step is loading the initial data, which is a .json file stroing the specific yield data for all german federal states for the year 2019 [data source]( https://www.umwelt-campus.de/institute/institut-fuer-betriebs-und-technologiemanagement/aktuelles/neue-ertragsstudie-zu-pv-dachanlagen-fuer-2019-veroeffentlicht). Therefore type in the terminal:
```sh
(env)$ python manage.py loaddata pv_yields.json
```
You should see a message in the terminal stating that 16 objects have been successfully installed. The installation is finished now. You can run a local server to to test the API now:
```
(env)$ python manage.py runserver
```
Navigate to `http://localhost:8000/api/pv_yields?state=by` using a browser, the curl command or an application like Postman. You should receive a json like this as response:

```
{"yield": 1140, "state": "by"}
```
For further details on how to use the app see the next section and use `http://localhost:8000` as `<Base_URL>`!

## Usage

You can either by installing the API on your local machine (following the instructions from the previous section and use `http://localhost:8000` as `<Base_URL>`) or you can access an already deployed version, using `https://cw-photovoltaik.herokuapp.com` as `<BASE_URL>`.

The API responds to two different types of queries:
### 1. Accessing the yield of a federal state
When given a german federal state, the API provides the specific yield of that federal state in the year 2019. Therefore, make a request with the format
``` <BASE_URL>/api/pv_yield?state=<STATE_CODE>```
State code is supposed to be replaced by a valid two-letter code for one of the german federal states (click [here](https://en.wikipedia.org/wiki/ISO_3166-2:DE) for more details about the german federal state codes). E.g.in order to access the value for Bavaria (BY), the request is: 
```
http://localhost:8000/api/pv_yield?state=by # for the local version, or
https://cw-photovoltaik.herokuapp.com/api/pv_yield?state=by # for the deployed version
```
The response will look be a json containing the state, which was given in the request, and its specific yield in kWh/kWp/year. For the example above, it should look like this: 

```
{"yield": 1140, "state": "by"}
```

### 2. Accessing the yield for a photovoltaik system, given its locations postcode and its capacity
When given a german postcode and the systems' capacity, the API provides a yield value of a photovoltaik system with the given capacity and location. Therefore the request follows the pattern
```
<BASE_URL>/api/pv_yield?plz=<POST_CODE>&capacity=<CAPACITY>
```
Here, `<POST_CODE>` is a placeholder for a valid german postcode (5 digits) and `<CAPACITY>` should be replaced by the systems' installed capacity in kWp. If you would like to get the yield of a system with a capacity of 10kWp, placed in 07349 Lehesten (Germany), you would want to make the request
```
http://localhost:8000/api/pv_yield?plz=07349&capacity=10 # for the local version, or
https://cw-photovoltaik.herokuapp.com/api/pv_yield?plz=07349&capacity=10 # for the deployed version
```
The response will be a json, containing the systems yield in kWh/year for the given location and capacity, and the federal state's code, where the given postcode is part of:
```
{"yield": 10900, "state": "th"}
```


## License
This software uses GNU General Public License
