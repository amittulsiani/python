import calendar
d31=[1,3,5,7,8,10,12]
d30=[4,6,9,11]
d28=[2]
global cal1

d1,m1,y1=(int(x) for x in input("Enter 1st date in the format dd-mm-yyyy: ").split('-'))

d2,m2,y2=(int(x) for x in input("Enter 2nd date in the format dd-mm-yyyy: ").split('-'))

if ((d1 > 31 or d2 >31) or (m1>12 or m2>12)):
    print ("Please enter valid date")

cal1 = 0
if (y1 ==y2):
    if (calendar.isleap(y1) and (m1!=m2) and (d1 or d2 > 28)):
        cal = 1
else:
    cal1 = calendar.leapdays(y2+1,y1-1)
    cal = abs(cal1)
nod=0
if (y1 > y2):
    dy= y1-y2
    m1= m1 + (dy*12)
    while (m2 < m1):
        if (m2 <= 12):
            if (m2 in d31):
                nod +=31
            elif (m2 in d30):
                nod += 30
            elif (m2 in d28):
                nod +=28
            m2 = m2 + 1
        elif (m2 > 12):
            m2 =1
            m1 = m1 - 12
    dd=(d1+nod)-d2
    print ("No of days between both dates is", dd + cal)
elif ((y1 == y2) and (m1==m2)):
    if (d1 == d2):
        print ("No of days between both dates is 0")
    elif (d2 > d1):
        print ("No of days between both dates is", d2 - d1)
    while (m2 < m1):
        if (m2 <= 12):
            if (m2 in d31):
                nod +=31
            elif (m2 in d30):
                nod += 30
            elif (m2 in d28):
                nod +=28
            m2 = m2 + 1
        elif (m2 > 12):
            m2 =1
            m1 = m1 - 12
        dd=(d1+nod)-d2
        print ("No of days between both dates is ", dd + cal)

elif (y2 > y1):
    d3,m3,y3= d1,m1,y1
    d1,m1,y1 = d2,m2,y2
    d2,m2,y2=d3,m3,y3
    dy= y1-y2
    m1= m1 + (dy*12)
    while (m2 < m1):
        if (m2 <= 12):
            if (m2 in d31):
                nod +=31
            elif (m2 in d30):
                nod += 30
            elif (m2 in d28):
                nod +=28
            m2 = m2 + 1
        elif (m2 > 12):
            m2 =1
            m1 = m1 - 12
    dd=(d1+nod)-d2
    print ("No of days between both dates is", dd + cal)
