for i in range(0,6):
    for j in range(i):
        print ("* ",end="")
    print (" ")

print ("\n")

for i in range(5,0,-1):
    for j in range (0,i):
        print ("* ",end="")
    print (" ")

print ("\n")

count =0
for i in range(8,0,-1):
        
    for j in range(i,0,-1):
        print(' ',end=' ')
             
    for k in range(0,count+1):  
        print('* ',end='')
    print(' ')
    count+=1

print ("\n")

count =0
for i in range(8,0,-1):
        
    for j in range(i,0,-1):
        print(' ',end=' ')
             
    for k in range(0,2*count+1):  
        print('* ',end='')
    print(' ')
    count+=1
    
