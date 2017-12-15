d31=0
d30=0
d28=0
d1=0
m1=0
d2=0
m2=0
nod=0
dy=0

def checkDays():
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
    return (d1+nod)-d2
