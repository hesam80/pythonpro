import sys
def cube(i) : 
	i = i * i * i
	

n = int(sys.argv[1])
total = 0.0
for i in range(1, n + 1):
	total += 1.0 / i
	print(total) 