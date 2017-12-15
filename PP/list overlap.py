a=[int(x) for x in raw_input("Enter first list ").split()]
b=[int(y) for y in raw_input("Enter second list ").split()]

print (a)
print (b)

c=[]

def common(x,y):
    for i in x:
        for j in y:
            if (i==j):
                c.append(i)
    print (c)

common(a,b)
    
