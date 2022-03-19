from atexit import register
import pymysql as sql
import time

class Login():
    con = sql.Connect(host='127.0.0.1', unix_socket='', user='root', password='', db='dbgame') 
    db = con.cursor() 
    def register(self):
        print('-'*20)
        print('Register')
        print('-'*20)
        
        name = input('Enter name: ')
        password = input('Enter password: ')
        counter = self.db.execute('SELECT length(id) FROM users;')
        query = "INSERT INTO users (id, name, password) VALUES (%s, %s, SHA(%s))"
        val = (counter+1, name, password)
        self.db.execute(query,val)

        self.con.commit()

    def login(self):
        while True:
            print('-'*20)
            print('Login')
            print('-'*20)

            name = input('Enter name: ')
            password = input('Enter password: ')
            query = 'SELECT name,password FROM users where name=%s and password=SHA(%s);'
            val = (name, password) 
            enter = self.db.execute(query, val)
            
            if enter==1:
                print('Login success!')
                time.sleep(1)
                break
            elif enter==0:
                print('Login unsuccess')
                time.sleep(1)
                answer=input('Do you wanna register? (Y/N) ')
                if answer.upper()=='Y':
                    self.register()
                    break
                elif answer.upper()=='N':
                    pass