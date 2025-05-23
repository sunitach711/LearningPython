import datetime
from time import strftime

x=datetime.datetime.now()
m=x.strftime("%Y")
m1=x=strftime("%y")
M=x=strftime("%M")
H=x=strftime("%H")
print(x)#output=2025-05-19 17:33:25.419895
print(m)#output=2025
print(m1)#output=25
print(M)#output=48
print(H)#output=17
print(datetime.datetime(2022,2,22))
#output=2022-02-22 00:00:00
