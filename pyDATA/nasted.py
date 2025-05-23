course={
    'php':{'duration':'3 months','fees':15000},
    'java': {'duration': '2 months', 'fees': 10000},
    'python': {'duration': '1 months', 'fees': 12000}
}
print(course)
course['java']['fees']=20000 #value update
print()
print(course['php']['fees'])
print()
for k,v in course.items():
    print(k,v['duration'],v['fees'])

    