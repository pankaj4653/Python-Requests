import requests

#r = requests.get('https://httpbin.org/get?page=2&count=2') 

payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params=payload)

print(r)  

#print(dir(r)) # if you ever want to know the attributes and methods associated with the object ...  run dir(Object)
#print(help(r)) # for much more detail

#print(r.text) #gives html document for the page in unicode   
#print(r.content) # gives data in Byte 

#with open('parker.png','wb') as f:
#	f.write(r.content)

print(r.status_code)
print(r.ok)
print(r.headers) # All the information in header
print(r.text)
print(r.url)


