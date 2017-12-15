a = raw_input("Enter a string - ")
b = []
for index,value in enumerate(a):
    b.append(value)
print b[::-1]

def reverse(text):
    revs = ""
    for i in text:
        revs = i + revs
    return (revs)

strig = raw_input("enter anything:")
print reverse(strig)

reverse(strig)
