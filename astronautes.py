import requests

r = requests.get('http://api.open-notify.org/astros.json', auth=('user', 'pass'))
for p in r.json()["people"]:
    print(p)
