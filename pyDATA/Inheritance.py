# Single Inheritance

class A:
    def displayA(self):
        print("Welcome to Wscubetech A")

class B(A):
    def displayB(self):
        print("Welcome to Wscubetech B")

obj=B()
obj.displayA()
obj.displayB()
#only obj B ka use krke A,B mathod ko call kr skte hai
#Welcome to Wscubetech A
#Welcome to Wscubetech B
