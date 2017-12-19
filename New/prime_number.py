def prime(num):
    factor_count = 0
    for i in range(2,num):
        if ((num % i) == 0):
            factor_count += 1

    if (factor_count > 0):
        print ("{} is not a prime number".format(num))
    else:
        print ("{} is a prime number".format(num))

a = int(input("Enter a number - "))
if (a <= 1):
    print ("Please enter a valid number")
else:
    prime(a)
