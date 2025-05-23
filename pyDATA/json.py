import json

d={
    'course_name':'Python',
    'fees':15000
}
f=json.dumps(d)
print(type(f))
print(f)
#output=<class 'str'>
#{"course_name": "Python", "fees": 15000}

