for i in range(0,6):
    for j in range(i):
        print (i,end=" ")
    print (" ")

print ("\n")

for i in range(1,7):
    for j in range(i):
        print (j,end=" ")
    print (" ")

print ("\n")

n = 1
for i in range(0,6):
    for j in range(i):
        print (n,end=" ")
        n += 1
    print (" ")

print ("\n")

x= int(input("Enter limit of Pyramid:"))
count=0
for i in range(x,1,-1):
    for j in range(i,1,-1):
        print (" ",end="")
    for k in range(1,count+1):
        print(count,end=" ")
    print(" ")
    count +=1
