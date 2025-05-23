l=[10,20,30,50,60]
t=len(l)
print(t)
for a in range(t):
    print(l[a])
    #l[0]=10
    #l[1]=20
print()
#without range
for a in l:
    print(a)
print()
#reverse
for a in range(t-1,-1,-1):
    print(l[a])

    