import pickle
import requests
import json
url="https://financialmodelingprep.com/api/v3/income-statement-as-reported/AAPL?apikey=demo"
respone=requests.get(url)
text=respone.text
text_dict=json.loads(text)
with open("Finance.pxl","ab") as f:
    pickle.dump(text_dict,f)

with open("Finance.pxl","rb") as f:
    file=pickle.load(f)
for i in text_dict:
    print(i)


# import pickle
# import requests
# url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# respons=requests.get(url)
# respons_text=respons.text
# data=respons_text.splitlines()
# red=[[i] for i in data]
# #pickling the python object
# fileobj=open('irisData.pkl','wb')
# pickle.dump(red,fileobj)
# fileobj.close()

# #Reading Of Pickel file
# fileobj=open('irisData.pkl','rb')
# data=pickle.load(fileobj)
# print(data)

