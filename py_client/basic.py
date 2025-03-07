import requests

endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint,params={"abc":123}) #http request
print(get_response.json()) #print response
#print(get_response.text) #print response

# HTML Request -> HTML Response
# REST API HTML Request -> JSON/XML Response

