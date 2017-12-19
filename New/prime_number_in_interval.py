def prime_interval(m,n):
    prime_list = []
    if ((m < 1) or (n < 1)):
        print ("Enter positive numbers only")
    elif (m < n):
        for i in range(m,n+1):
            if i > 1:
                for j in range(2,int(i/2)):
                    if ((i % j) == 0):
                        break
                else:
                    prime_list.append(i)
        print ("List of prime number between {0} and {1} is {2}".format(m,n,prime_list))
    else:
        print ("Starting Range should be less than ending range")

m = int(input("Enter starting interval - "))
n = int(input("Enter ending interval - "))
prime_interval(m,n)
