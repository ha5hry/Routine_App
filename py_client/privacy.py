import requests
from login import login
header = login()
endpoint = "http://127.0.0.1:8000/api/privacy/post-production-testing-bfiin/"
data = {"privacy": "Public"}
response = requests.post(endpoint, data, headers =header)
print(response.json())