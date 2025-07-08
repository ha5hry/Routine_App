import requests
from login import login

header = login()
endpoint = "http://127.0.0.1:8000/api/editl/sdkdkd-paunluks9ej7pnet344uo/"
routine_endpoint = requests.delete(endpoint, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)
