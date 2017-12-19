def swap(x,y):
    z=x
    x=y
    y=z
    print ("First Number after swapping is: {0}".format(x))
    print ("Second Number after swapping is: {0}".format(y))

a = int(input("Enter first number - "))
b = int(input("Enter second number - "))
swap(a,b)
