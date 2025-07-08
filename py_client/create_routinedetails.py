import requests
from login import login

header = login()
endpoint = "http://127.0.0.1:8000/api/edit/details/hdksd-6cjco6aohpckewbthstax/"
data = {"title": "is Testing successful"}
routine_endpoint = requests.patch(endpoint, json=data, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)
