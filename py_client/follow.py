from login import login
import requests

header = login()
endpoint = 'http://127.0.0.1:8000/api/profile/thirduser/follow/'
data = {'follow':'follow'}
follow_endpoint = requests.post(endpoint ,json = data, headers= header)
endpoint_response = follow_endpoint.json()



