#random.randint(a,b)
#This returns a number N in the inclusive range [a,b], meaning a <= N <= b, where the endpoints are included in the range.

def random(a,b):
    import random
    print ("Random Number is - {}".format(random.randint(a,b)))

a,b = input("Enter two numbers to find a random number between them - ").split()
random(int(a),int(b))
