def simplefunction():
    print("Welcome to Wscubetech")
simplefunction()
simplefunction()
simplefunction()
print()

def sumdata(a,b):
    print(a+b)
sumdata(20,10)
#output=30
def sumdata(a,b=5):
    print(a+b)
sumdata(20)
#output=25
print()
def sumdata(a,b=5):
    c=a+b
    return c
output=sumdata(20,10)
print(output)
#output=30
