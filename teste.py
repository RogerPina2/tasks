import requests

from datetime import datetime

url = 'http://localhost:8000'

headers = {"Content-type": "application/json"}

json={
    'title': 'oi',
    'pub_date': str(datetime.now()),
    'description': 'oi'
}


r = requests.put('{}/tasks/{}'.format(url,2), json=json, headers=headers)

print(r.content)

