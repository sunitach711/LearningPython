import json

file=open("jsondata.py","r")
x=file.read()
finaldata=json.loads(x)

print(finaldata['name'])
print(finaldata['courses'][0]['title'])


