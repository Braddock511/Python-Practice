import pymysql as sql
import time

con = sql.Connect(host='127.0.0.1', unix_socket='', user='root', password='', db='dbgame') 
db = con.cursor() 

class Login():
    def register(self):
        name = input('Enter name: ')
        password = input('Enter password: ')
        counter = db.execute('SELECT length(id) FROM users;')
        query = "INSERT INTO users (id, name, password) VALUES (%s, %s, SHA(%s))"
        val = (counter+1, name, password)
        db.execute(query,val)

        con.commit()

    def login(self):
        name = input('Enter name: ')
        password = input('Enter password: ')
        query = 'SELECT COUNT(*) FROM users where name=%s and password=SHA(%s);'
        val = (name, password) 
        enter=db.execute(query,val)
        if enter==1:
            print('Login success!')
            time.sleep(1)
            pass
        else:
            print('Login unsuccess')

asd = Login()

asd.login()