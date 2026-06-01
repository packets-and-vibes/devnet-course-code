import requests

base_url = "https://swapi.info/api/"
endpoint = "people/"
# Response object
response = requests.get(base_url + endpoint)
data = response.json()

#print(data[0])
print(data[0]['name'])