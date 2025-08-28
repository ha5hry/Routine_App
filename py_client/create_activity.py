import requests
from login import login
import datetime
now = datetime.datetime.now()
start_time = now.strftime('%H:%M')
later_time = now + datetime.timedelta(hours=1)
end_time = later_time.strftime('%H:%M')
header = login()
endpoint = "http://127.0.0.1:8000/api/create/routine/add/post-production-testing-bfiin/"
data = {'activity_name':"Post production", 'start_time': start_time, 'end_time': end_time}
routine_endpoint = requests.post(endpoint, json=data, headers=header)
routine_response = routine_endpoint.json()
print(routine_response)
