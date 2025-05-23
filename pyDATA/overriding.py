class A:
    def showdata(self):
        print("I m in A class")

class B(A):
    def showdata(self):
        print("I m in B class")

obj=B()
obj.showdata()
#outpput=I m in B class


