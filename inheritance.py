class parent:
    def __init__(self):
        print ("Parent Constructor")

    def parentMethod(self):
        print ("Parent Method")

class child(parent):
    def __init__(self):
        print ("Child Constructor")

    def childMethod(self):
        print ("Child Method")

c = child()
c.childMethod()
c.parentMethod()

class grandchild(child):
    def __init__(self):
        print ("Grandchild Constructor")

    def grandchildMethod(self):
        print ("Grandchild Method")

g = grandchild()
g.grandchildMethod()
g.childMethod()
g.parentMethod()


print (issubclass(child,parent))
print (isinstance(c,parent))
