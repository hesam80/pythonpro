#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
import hello
print("Content-Type: text/html\n charset:utf-8\n")
hello.hellos()
x=12
y=2
#hello.is_prime(x , y)
#s= y % x
#print("s=%s" %s)
#for i in range(x , x+y):
   # hello.is_prime(i , y)
x = int(x)
y = int(y)
s = x+y
while x < s :
   hello.is_prime(x,y)
   x=x+1

print("thats it")
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 