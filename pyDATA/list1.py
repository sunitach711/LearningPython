l=[1,2,3,4,5]
print(type(l))
print(l[2])

l=[1,2,3,[4,5,6]]
print(l[3][1])

# mix list
l=[2,3,"Hello",[3,4,5]]
print(l[2])

#list slicing
l=[2,3,"Hello",[3,4,5]]
print(l[0:3])
print(l[1:])

l=[1,2,3,4,5,6]
print(l[3:])
print(l[0::2]) #2 ka increment
#::=end tk read
#reverse
print(l[-1::-1])
print(l[-1::-2])

