import requests
from login import login

header = login()
endpoint = 'http://127.0.0.1:8000/api/routine/title/'
data = {'title': 'Testing title two', 'description': 'Checking for the id and slug'}
routine_endpoint = requests.post(endpoint, json=data, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)