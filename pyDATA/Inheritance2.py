# Multipal Inheritance

class A:
    def displayA(self):
        print("Welcome to Wscubetech A")

class B:
    def displayB(self):
        print("Welcome to Wscubetech B")

class C(A,B):
    def displayC(self):
        print("Welcome to Wscubetech C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

#Welcome to Wscubetech A
#Welcome to Wscubetech B
#Welcome to Wscubetech C