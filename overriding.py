class parent:
    def myMethod(self):
        print ("Parent Method")

class child(parent):
    def myMethod(self):
        print ("Child Method")

inst = child()
#Instance of child class
inst.myMethod()


inst = parent()
#Instance of Parent class
inst.myMethod()


print (str(inst))

