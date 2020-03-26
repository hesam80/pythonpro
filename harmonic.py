import sys
import random
import stdio

def harmonic(n):
  total = 0.0
  for i in range(1 , n + 1):
    total = 1.0 / i
  return total

def hermichian(n, r=2):
 total=0.0
 for i in range(1, n+1):
	total= 1.0/(i**r)
 return total

for i in range(1, len(sys.argv)):
		arg = int(sys.argv[i])
	if arg == 2 :
		value = harmonic(arg)
		print(value)
	else :
      print('hello , end = " "')