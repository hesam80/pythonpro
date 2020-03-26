#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
import xlrd 


print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("content-type: text/html\n\n" )
print("<br><B>hello python</B>")
print("<h1> my statement here </h1>")
s=2
print(s)
print("""<li><a href="tst.py">go to tst python</a></li>""")
print("""<li><a target="_blank" href="openfile.py">go to openfile python</a></li>""")
print("""<li><a target="_blank" href="dictionarytst.py">go to dictionarytst python</a></li>""")
print("""<li><a href="dictionarytst.py">dictionarytst</a></li>""")
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']