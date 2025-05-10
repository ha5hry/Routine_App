import requests
from getpass import getpass
def register_user():
    endpoint = 'http://127.0.0.1:8000/api/register/'
    email = input("Input your email?\n")
    password = getpass("Input your password?\n")
    password2 = getpass("Confirm your password?\n")
    data = {'username': 'seconduser', 'email':email, 'first_name': 'Second', 'last_name': 'person', 'gender':'m', 'password': password, 'password2': password2}
    register_endpoints= requests.post(endpoint, json=data)
    endpoint_response = register_endpoints.json()
    print(endpoint_response)
    return endpoint_response


def add_skill( header):
    endpoint = 'http://127.0.0.1:8000/api/skill/'
    data = {'skill':'backend_development'}
    skill_endpoint = requests.post(endpoint, json=data, headers=header)
    endpoint_response = skill_endpoint.json()
    print(endpoint_response)
    return endpoint_response
if __name__ == '__main__':
    register_user()
