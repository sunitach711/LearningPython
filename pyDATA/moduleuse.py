import module
print(module.sum(10,20)) #output=30
print(module.mul(10,20)) #output=200

import module as m
print(m.sum(10,20)) # output=30
print()
from module import sum
print(sum(10,20)) #output=30
from module import *
print(sum(10,20)) #output=30
print(mul(10,20)) #output=200

