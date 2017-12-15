def A(word):
    def inner():
        print ("Amit")
    return inner

@A
def func():
    return inner()
