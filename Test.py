#łączenie z bazą danych
import pymysql as mysql

con = mysql.Connect(host='127.0.0.1', unix_socket='', user='root', password='', db='dbgame') 
cur = con.cursor() 
cur.execute("SELECT * FROM characters") 

for record in cur:
    for x in record:
        print(x) 

cur.close()