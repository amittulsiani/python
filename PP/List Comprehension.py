lis = [int(a) for a in raw_input("Enter few numbers - ").split()]
new = []
for i in lis:
    if (i % 2 == 0):
        new.append(i)

print (new)
