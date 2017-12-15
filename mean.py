num = [int(x) for x in input("Enter few numbers: ").split()]
tot = len(num)
print ("Total Numbers Entered :", tot)
sum1 = 0
for i in range(tot):
    sum1 += num[i]

print ("Mean of", tot, "numbers is", sum1/tot)
