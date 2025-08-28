import requests
from login import login

header = login()
endpoint = "http://127.0.0.1:8000/api/routine/tracker/"
endpoint_response = requests.get(endpoint, headers = header)
print (endpoint_response.json())