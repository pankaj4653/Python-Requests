import requests

payload = {'name':'Pankaj', 'password':'pankaj4653'}

r = requests.post('https://httpbin.org/post', data = payload)

print(r.text)

print(r.url)

#print(r.json())   

r_dict = r.json()

print(r_dict['form'])