class parent:
    counter=10
    def __init__(self):
        print("class initialized")
    def parentfunc(self):
        print("parentfunc being called")
    def setCounter(self, num):
        parent.counter=num
    def showCounter(self):
        print(str(parent.counter))

class child(parent):
    def __init__(self):
        print("child class being initialized")
    def childfunc(self):
        print("child func being called")
