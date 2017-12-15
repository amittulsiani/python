def mean(*num):
    sum1 = 0
    for i in num:
        sum1 += i
    print ("Mean of",num,"is", sum1/len(num))

mean(1,2,3)

mean(-8,10,-12,32,-60,48,18)

mean(10,25,35,5,-15,0)
