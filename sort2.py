num = [int(y) for y in input().split()]
print (num)
n = len(num)
print ("Length : " , n)

for i in range(n):
    for j in range(n - 1):
        if (num[j] > num[j + 1]):
            num[j+1],num[j] = num[j],num[j+1]


print ("Sorted List: " , num)
