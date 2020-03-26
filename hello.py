import sys
def hellos():
   print("hello.py Directory %s" %__file__)


def is_prime(n , m):
    if n < 2 : 
        print("this is 1 prime %s" %n)
        
    
    s = n % 2
    if  s == 0 : 
       print("this is not prime %s" %n)
    else :
      print("this is  prime %s" %n)
