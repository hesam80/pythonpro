#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
import stdio
n = stdio.readInt()
counts = [[0]* n for i in range(n)]
degrees = [0] * n
while not stdio.isEmpty():
	i = stdio.readInt()
	j = stdio.readInt()
degrees[i] += 1
counts[i][j] +=1
print('%d %d' % (n,n))
# for i in range(n) :
# 	 for j in range(n):
# 		#p = (.9 * (counts[i][j] / degrees[i])) + (0.1 / n)
# 	  p = counts[i][j]
# 	  q = degrees[i]
# 	  f = q*p
# 	 print(p)
# 	 print(q)
# print(f)pandas/io/excel/_base.py