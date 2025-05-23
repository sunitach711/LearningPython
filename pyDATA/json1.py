import json

d='{"cname":"Python","fees":8000,"duration":"2Months"}'
x=json.loads(d)

print(x,type(x))
for a in x:
    print(a,x[a])

#{'cname': 'Python', 'fees': 8000, 'duration': '2Months'} <class 'dict'>
#cname Python
#fees 8000
#duration 2Months
