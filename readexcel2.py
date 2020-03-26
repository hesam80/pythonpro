#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe

# from pandas import ExcelWriter
# from pandas import ExcelFile
# import xlrd 
# import stdio
# print("Content-Type: text/html\n charset:utf-8\n")
# def hello(request):
    # return HttpResponse("Hello world")
    # print("Content-Type: text/html\n charset:utf-8\n")
# print("<br><B>hello python</B>")
#df = pd.read_excel('tst.xlsx', sheetname='Sheet1')

# print("Column headings:")
# print(df.columns)

import xlrd 


print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("content-type: text/html\n\n" )
print("<br><B>hello python</B>")
  
# Give the location of the file 
loc = ('tst.xlsx') 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sotoon = int(sheet.ncols) 
satr = int(sheet.nrows)
# For row 0 and column 0 
print(sheet.cell_value(0, 0))
print("tedade sadr va sotoon ")
print(satr)
print(sotoon)
i = 0
for i in range(0,2):
	
	print(sheet.cell_value(i, 0))
	i+=1
dic ={"status":200,"message":"ok"}
print(dic['status'])