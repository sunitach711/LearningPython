d={ 'name': 'python',
    'fees': '8000',
    'duration': '2months'}
del d['fees']
print(d)
print()
d={ 'name': 'python',
    'fees': '8000',
    'duration': '2months'}
a=d.pop('fees')
print(a)
print(d)

