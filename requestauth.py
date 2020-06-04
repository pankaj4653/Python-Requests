import requests


r = requests.get('https://httpbin.org/basic-auth/Pankaj/pankaj4653', auth=('Pankaj', 'pankaj4653'))



print(r.json())