import time
from datetime import date

class Login:
    def __init__(self, con, db):
        self.con = con 
        self.db = db
     
    def register(self):
        print('-'*20)
        print('Register')
        print('-'*20)
        
        self.name = input('Enter name: ')
        password = input('Enter password: ')
        counter = self.db.execute('SELECT length(id) FROM users;')
        query = "INSERT INTO users (id, name, password) VALUES (%s, %s, SHA(%s))"
        val = (counter+1, self.name, password)
        self.db.execute(query,val)

        print('Choose character: ')
        print('1. Warrior')
        print('2. Wizard')
        print('3. Archer')
        print("")

        self.choose_character = int(input('Choose: '))
        print('-'*20)
        query1 = f'SELECT hp, damage, agility, intelligence, speed FROM characters WHERE id={self.choose_character}'
        self.db.execute(query1)
        self.character = [statistics for statistics in self.db]
        if self.choose_character==1:
            print('Choose weapon: ')
            print('1. Sword')
            print('2. Axe')
            print('3. Spear')
            print("")
        if self.choose_character==2:
            print('Choose weapon: ')
            print('4. Fire wand')
            print('5. Wind wand')
            print('6. Lighting wand')
            print("")
        if self.choose_character==3:
            print('Choose weapon: ')
            print('7. Short bow')
            print('8. Long bow')
            print('9. Crossbow')
            print("")

        self.choose_weapon = int(input('Choose: '))
        query2 = f'SELECT attack, speed_attack, weight FROM weapons WHERE id={self.choose_weapon}'
        self.db.execute(query2)
        self.weapon = [statistics for statistics in self.db]
        self.con.commit()
    

    # @__init__ #nowe polaczenie po wprowadzeniu danych
    def add_to_main(self):
        counter2 = 'SELECT COUNT(id) FROM main'
        id_user = f'SELECT id FROM users WHERE name={self.name}'
        id_character = f'SELECT id FROM characters WHERE id={self.choose_character}'
        query3 = f"INSERT INTO main VALUES ({self.db.execute(counter2)+1},{self.db.execute(id_user)}, {self.db.execute(id_character)}, {date.today()})"
        self.db.execute(query3)
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