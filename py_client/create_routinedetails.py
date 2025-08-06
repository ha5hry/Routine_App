import requests
from login import login

header = login()
endpoint = "http://127.0.0.1:8000/api/routine/title/"
data = {"title": "Post production testing", "description": "Let see"}
routine_endpoint = requests.post(endpoint, json=data, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)
