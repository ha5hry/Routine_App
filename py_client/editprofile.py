import requests
from login import login
header = login()
endpoints = 'http://127.0.0.1:8000/api/edit/profile/'
data = {'username': 'useradmin'}
edit_endpoints = requests.patch(endpoints, json=data, headers=header)
endpoints_response = edit_endpoints.json()
print (endpoints_response)