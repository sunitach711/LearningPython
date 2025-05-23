class DemoClass:
    a=10
    def __init__(self):
       print("Welcome to Wscubetech")
#output= Welcome to Wscubetech ( Constructors ko call krne ki jrurt nhi hai
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
#output=100
obj.showvalue1(20,30)
#output=50

