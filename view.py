#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
from HTMLParser import HTMLParser
import hello
print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse()
    print("content-type: text/html\n\n" )
print("<br><B>hello python</B>")
print ("""
    <H1>CGI script ! Python</H1>
    <H2>This is my first CGI script</H2>
    """)
print("""<li><a href="tst.py">go to tst python</a></li>""")
x=12
y=2

x = int(x)
y = int(y)
s = x+y

print("""<li><a href="tst.py">go to tst python</a></li>""" , s)
