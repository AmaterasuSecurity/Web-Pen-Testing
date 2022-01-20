import requests

payload = {'url':'http://edge-security.com'} # creating payload
#r = requests.get('http://httpbin.org/ip')
r = requests.get('http://httpbin.org/redirect-to',params=payload) # adding redirect string and params
# print(r.text)
print("t *" + str(r.status_code))