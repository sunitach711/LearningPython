#overriding

class Parent:
    def displayinfo(self):
        print("Welcome to Wscubetech")

class Child(Parent):
    def displayinfo(self):
        super().displayinfo()
#super()=Class Parent ke function ko call krne ke liye
#agr super function ka use nhi krte hai to class child class parent ko
#overwrite kr degi
        print("Child Info")

obj=Child()
obj.displayinfo()
#Welcome to Wscubetech
#Child Info