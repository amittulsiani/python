a = [int(x) for x in raw_input("Enter few numbers - ").split()]
b=[]
def comp(z):
    for i in z:
        count = 0
        if (i in b):
            continue
        else:
            for j in z:
                if (i == j):
                    count = count + 1
        b.append(i)
        print 'Repeating Word', i
        print 'Total Occurence', count
comp(a)
