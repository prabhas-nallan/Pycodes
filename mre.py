import requests
import json

r=requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo")

print(r)
in_string=r.content
in_dict=json.loads(in_string)
a=in_dict
print(a[0]["symbol"])
# print(in_string["beta"])
print(r.status_code)

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

# print(x.content)
print(x.status_code)