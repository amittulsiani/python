for num in range(1,100):
    for i in range(2,num):
        if (num%i == 0):
            j = num/i
            print (num, " divides ", i ," == " , j)
            break
    else:
        print(num, " is a prime number")


