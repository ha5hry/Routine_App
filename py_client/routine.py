import requests
from login import login

header = login()
endpoint = 'http://127.0.0.1:8000/api/create/routine/'
data = {'title': 'The new beginning', 'description': 'Wannabe Dev'}
routine_endpoint = requests.post(endpoint, json=data, headers=header)
routine_reponse = routine_endpoint.json()
print(routine_reponse)