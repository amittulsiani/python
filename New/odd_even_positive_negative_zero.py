def num_info(num):
    if (num > 0):
        print ("{} is greater than zero".format(num))
    elif (num < 0):
        print ("{} is lower than zero".format(num))
    else:
        print ("{} is equal to zero".format(num))

    if ((num % 2) == 0):
        print ("{} is Even number".format(num))
    else:
        print ("{} is Odd number".format(num))

a = int(input("Enter a number - "))
num_info(a)
