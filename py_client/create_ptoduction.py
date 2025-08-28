import requests 
from login import login
header = login()
endpoint = "https://routineapp-production.up.railway.app/api/routine/title/"
data = {"title": "First Title in production environment", "description": "Sheesh"}
routine_endpoint = requests.post(endpoint, json=data, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)
