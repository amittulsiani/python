val = 65
for i in range(0, 5):
	for j in range(0, i+1):
		ch = chr(val)
		print(ch, end=" ")
	val = val + 1
	print()

print ("\n")
val = 69
for i in range(6,0,-1):
	for j in range(i,1,-1):
		ch = chr(val)
		print(ch, end=" ")
	val = val - 1
	print()
