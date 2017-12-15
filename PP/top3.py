a = [int(x) for x in raw_input("Enter few numberes - ").split()]
p = []
q = []
def top3a(z):
    for i in range(3):
        b = max(z)
        p.append(b)
        z.remove(b)
    print 'Top 3 numbers are - ', p
    print 'Remaining Digits - ', a
top3a(a)

b = [int(x) for x in raw_input("Enter few numberes - ").split()]
def top3b(z):
    c = sorted(z)
    q = c[-3:]
    print 'Top 3 numbers are - ',sorted(q,reverse=True)
    print 'Original List - ',z

top3b(b)

