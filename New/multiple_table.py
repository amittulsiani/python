def table(num):
    for i in range(1,11):
        print ("{0} * {1} = {2}".format(num,i,num*i))

a = int(input("Enter a number - "))
table(a)
