from login import login
import requests

header = login()
endpoint = 'http://127.0.0.1:8000/api/myprofile/'
follow_endpoint = requests.get(endpoint ,headers= header)
endpoint_response = follow_endpoint.json()

