num = int(raw_input("Enter a number "))
for i in range(num,0,-1):
    if (num % i == 0):
        print (i, "is a divisor")

