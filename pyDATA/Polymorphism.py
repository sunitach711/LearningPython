# l=[10,20,30,40]
# print(len(l))
#output=4
# s="Welcome"
# print(len(s))
#output=7

#overloading
class Ws:
    def displayinfo(self,name=''):
        print("Welcome to Wscubetech"+name)

obj=Ws()
obj.displayinfo() #output=Welcome to Wscubetech
obj.displayinfo('Python')
#output=Welcome to WscubetechPython
