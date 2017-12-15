def entryExit(func):
    def funcM():
        print("Before calling")
        func()
        print ("After calling")
    return funcM


@entryExit
def func1():
    print("inside func1()")

@entryExit
def func2():
    print("inside func2()")


func1()

print ("\n")

func2()
