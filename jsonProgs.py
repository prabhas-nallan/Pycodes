import json

#Converting from string to dict we use json.loads()
data='{"tarun":"VsCode","Prabhas":"Visual studio"}'
print(data)
converting_dict=json.loads(data)
for i in range(0,3):
    print(converting_dict["tarun"])

#Reading the json file we use json.load()

with open("person.json") as f:
    json_file=json.load(f)
print(json_file)

#Converting from dict to json we use json.dumps()

dict1={"Tarun":"Dell 3000","Prabhas":"Dell 5000","Hates":False}
json_dict=json.dumps(dict1)
print(json_dict)

#To write a json file in Python we use json.dump()

nums={
    1:2,
    2:3,
    3:4
}

with open("numbers.txt","a") as f2:
    json_file_inPython=json.dump(nums,f2)

#Sort keys
person_str='{"Name":"Tarun","Laptop":"Dell 3000"}'
person_dict=json.loads(person_str)
print(json.dumps(person_dict,indent=4,sort_keys=True))

