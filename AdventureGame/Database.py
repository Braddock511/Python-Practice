import time
import psycopg2 as sql

        
class Db():
    def __init__(self, host, port, db, user, password):
        self.conn = sql.connect(host = host, port = port, database = db, user = user, password = password)
    
    #adding new user to table users
    def new_user(self):
        print('-'*20)
        print('Register')
        print('-'*20)

        self.name = input('Enter name: ')
        password = input('Enter password: ')
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute('SELECT count(*) FROM users;')
                id = curs.fetchall()[0][0]
                curs.execute(f"INSERT INTO users VALUES ({id+1}, '{self.name}', ENCODE('{password}', 'hex'))")

    #adding new character to table characters and weapon to table weapons
    def new_character(self):
        #character
        print('-'*20)
        print('Choose character: ')
        print('1. Warrior')
        print('2. Wizard')
        print('3. Archer')
        print("")

        self.choose_character = int(input('Choose: '))
        print('-'*20)

        #weapon
        if self.choose_character == 1:
            print('Choose weapon: ')
            print('1. Sword')
            print('2. Axe')
            print('3. Spear')
            print("")
        if self.choose_character == 2:
            print('Choose weapon: ')
            print('4. Fire wand')
            print('5. Wind wand')
            print('6. Lighting wand')
            print("")
        if self.choose_character == 3:
            print('Choose weapon: ')
            print('7. Short bow')
            print('8. Long bow')
            print('9. Crossbow')
            print("")

        self.choose_weapon = int(input('Choose: '))

    #user login
    def login(self):
        while True:
            print('-'*20)
            print('Login')
            print('-'*20)

            self.name = input('Enter name: ')
            password = input('Enter password: ')
            with self.conn:
                with self.conn.cursor() as curs:
                    query = f"SELECT count(*) FROM users where name='{self.name}' and password=ENCODE('{password}', 'hex');"
                    curs.execute(query)
                    enter = curs.fetchall()[0][0]
            
            if enter==1:
                print("")
                print('Login success!')
                time.sleep(1)
                break
            else:
                print("")
                print('Login unsuccess')
                time.sleep(1)
                answer=input('Do you wanna register? (Y/N) ')
                if answer.upper()=='Y':
                    self.new_user()
                    break
                elif answer.upper()=='N':
                    pass

    #adding data to main table
    def add_to_main(self):
        try:
            with self.conn:
                with self.conn.cursor() as curs:
                    curs.execute('SELECT count(*) FROM main;')
                    id = curs.fetchall()[0][0]

                    curs.execute(f"SELECT id FROM users WHERE name='{self.name}';")
                    id_user = curs.fetchall()[0][0]

                    curs.execute('SELECT CURRENT_DATE')
                    date = curs.fetchall()[0][0]
                    
                    curs.execute(f"INSERT INTO main VALUES ({id+1},{id_user}, {self.choose_character}, {self.choose_weapon}, '{date}')")

        except sql.ProgrammingError:
            with self.conn.cursor() as curs:
                    curs.execute('SELECT count(*) FROM main;')
                    id = curs.fetchall()[0][0]

                    curs.execute(f"SELECT id FROM users WHERE name='{self.name}';")
                    id_user = curs.fetchall()[0][0]

                    curs.execute('SELECT CURRENT_DATE')
                    date = curs.fetchall()[0][0]
                    
                    curs.execute(f"INSERT INTO main VALUES ({id+1},{id_user}, {self.choose_character}, {self.choose_weapon}, '{date}')")
            

    #choosing charcter after login
    def user_character(self):
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(f"SELECT ch.name, w.name FROM characters as ch, weapons as w, main as m, users as u WHERE m.id_character=ch.id and m.id_weapon=w.id and m.id_user=u.id and u.name='{self.name}';")
                characters = curs.fetchall()

                while True:
                    print('1. Choose already created hero')
                    print('2. Create new hero')
                    print("")
                    answer = int(input('Choose: '))
                    if answer==1:
                        print("")
                        for i, character in enumerate(characters):
                            weapons = character[1].split("_")
                            try:
                                print(f'{i+1}. {character[0]} with {weapons[0].capitalize()} {weapons[1]}') 
                            except IndexError:
                                print(f'{i+1}. {character[0]} with {weapons[0].capitalize()}') 

                        print("")
                        id_charcter = int(input('Choose your hero: '))
                        self.character = (characters[id_charcter-1][0])
                        self.weapon = (characters[id_charcter-1][1])
                        break

                    else:
                        self.new_character()
                        self.add_to_main()
                        print("")
                        print('New hero created!')
                        time.sleep(1)
                
                
    #get stats of user character
    def user_stats(self):
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(f"SELECT * FROM characters WHERE name='{self.character}'")
                stats_character = curs.fetchall()[0]

                curs.execute(f"SELECT * FROM weapons WHERE name='{self.weapon}'")
                stats_weapon = curs.fetchall()[0]

        return stats_character, stats_weapon

    #executing query from db
    def execute(self, query):
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(query)
                return curs.fetchall()

    def get_name(self):
        return self.name

    #closing connection
    def close(self):
        return self.conn.close()