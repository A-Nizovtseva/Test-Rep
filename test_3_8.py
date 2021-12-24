##import pymssql  
##
##conn = pymssql.connect(server=r'N-PC\SQLEXPRESS',
##                       user='N-PC\n',
####                      password='',
##                       database='Draft')  
######cursor = conn.cursor()  
######cursor.execute('select top 1000 MaterialId, MaterialName  from [Draft].[dbo].[Material];')  
######row = cursor.fetchone()
######while row:  
######    print ( str(row[0]) + " " + str(row[1]) )    
######    row = cursor.fetchone()
####
####from os import getenv
####import pymssql
####server = getenv("PYMSSQL_TEST_SERVER")
####user = getenv("PYMSSQL_TEST_USERNAME")
####password = getenv("PYMSSQL_TEST_PASSWORD")
####print (server, user, password)
####conn = pymssql.connect('N-PC\SQLEXPRESS', '', '', "Draft")
##
####conn = pymssql.connect(
####    host=r'N-PC\SQLEXPRESS',
####    user=r'',
####    password='',
####    database='Draft')
##
##print(pymssql.VERSION)

import pyodbc
##'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
##';DATABASE='+database+';UID='+username+';PWD='+ password)
##cnxn = pyodbc.connect(     'DRIVER={ODBC Driver 11 for SQL Server};'+
##    'SERVER=N-PC\SQLEXPRESS;DATABASE=Draft;UID=N-PC\n;PWD= ')
##cnxn = pyodbc.connect(     'DRIVER={ODBC Driver 11 for SQL Server};'+
##    'SERVER=N-PC\SQLEXPRESS;DATABASE=Draft;UID=N-PC\n;PWD=;')
cnxn = pyodbc.connect(driver='{ODBC Driver 11 for SQL Server}',
                      server='N-PC\SQLEXPRESS', 
                      database='Draft',               
                      trusted_connection='yes')
cursor = cnxn.cursor()
cursor.execute("select top 1000 MaterialId, MaterialName  from [Draft].[dbo].[Material];")
rows = cursor.fetchall()
for row in rows:
    print( row.MaterialId )
