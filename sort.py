num = [int(x) for x in input().split()]
print (num)

newList = []

while num:
    mini = num[0]
    for x in num:
        if (x < mini):
            mini = x
    newList.append(mini)
    num.remove(mini)

print ("\nSorted List : " , newList)


