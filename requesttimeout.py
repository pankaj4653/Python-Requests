import requests

r = requests.get('https://httpbin.org/delay/4', timeout=5)

print(r.json())