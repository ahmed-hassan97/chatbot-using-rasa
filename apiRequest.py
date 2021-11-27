# importing the requests library
import requests


## function to get all country
def getAllCountry():
    API_ENDPOINT = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
    try:
        r = requests.get(API_ENDPOINT).json()   
    except requests.exceptions.HTTPError as e:
        print (e)  
    return r['body']

## function to send request and get capital of country
def getCapitalOfCountry(country):
    # defining the api-endpoint 
    API_ENDPOINT = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
    ## validate if country is found or not 
    allCountry = getAllCountry()
    if(country not in (allCountry)):
        return "name of this country is not found in request please try another country"
    # data to be sent to api
    data = {
            "country": country
           }
    headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ****'
              }
    try:
        response = requests.request("POST", API_ENDPOINT, headers=headers,json=data)
    except requests.exceptions.HTTPError as e:
        print ("error there are problem in post request may be country not found please try another country")  
    # extracting response text 
    response = response.text.encode('utf8')
    return response

## function to send request and get Population of a Country 
def getPopulationOfCountry(country):
     # defining the api-endpoint 
    API_ENDPOINT = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation"
    ## validate if country is found or not 
    allCountry = getAllCountry()
    if(country not in (allCountry)):
        return "name of this country is not found in request please try another country"
 
    # data to be sent to api
    data = {
            "country": country
           }
    headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ****'
              }
    try:
        response = requests.request("POST", API_ENDPOINT, headers=headers,json=data)
    except requests.exceptions.HTTPError as e:
        print ("error there are problem in post request may be country not found please try another country")  
    # extracting response text 
    response = response.text.encode('utf8')
    return response    
  
print(getPopulationOfCountry("Australia"))