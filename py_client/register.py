import requests
from getpass import getpass
endpoint = 'http://127.0.0.1:8000/api/register/'
email = input("Input your email?\n")
password = getpass("Input your password?\n")
data = {'username': 'firstuser', 'email':email, 'first_name': 'First', 'last_name': 'person', 'gender':'m', 'password': password}
register_endpoint = requests.post(endpoint, json=data)
print(register_endpoint.json())
