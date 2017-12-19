def factorial(num):
    f = 1
    if (num < 0):
        print ("Enter positive number")
    elif (num == 0):
        print ("Factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            f = f*i
        print ("Factorial of {0} is {1}".format(num,f))

a = int(input("Enter a number - "))
factorial(a)
