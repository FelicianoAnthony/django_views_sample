import requests 
from pprint import pprint
from json import dumps

url = 'http://10.157.164.235:8000/coins/99/'

response = requests.get(url)

def print_status(r):
    print('URL={}\nStatus Code={}\nReason={}'.format(r.url, r.status_code, r.reason))


#print_status(response)


obj = {
    "_id": 99,
    "name": "name here",
    "website": "http://www.",
    "exchange_id": "exchange_id here"
    }


post_response = requests.post(url, data=dumps(obj))

print_status(post_response)

print(post_response.text)