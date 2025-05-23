class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1=Area()
obj1.find_area(10,20)
#output=200
obj1.find_area(10)
#output=100
obj1.find_area()
#output=Nothing