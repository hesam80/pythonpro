#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
import sys
import stdio
import random
print("Content-Type: text/html\n charset:utf-8\n")
n= len(sys.argv)
print("command line is %s" %n)
print(random.random())
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')