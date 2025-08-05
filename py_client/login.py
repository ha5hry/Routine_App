import requests
from getpass import getpass
from register import add_skill

def login():
    endpoints = 'http://127.0.0.1:8000/api/create-token/'
    email = input("Input your email?\n")
    password = getpass("Input your password?\n")
    login_endpoint = requests.post(endpoints, json = {'email': email, 'password':password})
    endpoint_response = login_endpoint.json()
    print (endpoint_response)
    if login_endpoint.status_code == 200:
        access_code =  endpoint_response["access"]
        print(access_code)
        header = {
            'AUTHORIZATION': f'Bearer {access_code} '
        }
    return header

if __name__ == '__main__':
    header = login()
    


    