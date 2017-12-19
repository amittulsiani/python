def fibonacci(limit):
    a = 0
    b = 1
    list = [0,1]
    for i in range(limit-2):
        c = a+b
        a = b
        b = c
        list.append(c)
    print ("Fibonacci list - {}".format(list))

lim = int(input("Enter a number - "))
fibonacci(lim)
