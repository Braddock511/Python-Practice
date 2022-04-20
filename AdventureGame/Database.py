import time
import psycopg2 as sql
from dataclasses import dataclass

@dataclass
class Db():
    host: str
    port: int
    db: str
    user: str
    password: str

    def __post_init__(self) -> None:
        self.conn = sql.connect(host = self.host, port = self.port, database = self.db, user = self.user, password = self.password)
    
    #adding new user to table users
    def new_user(self) -> None:
        print('-'*20)
        print('Register'.center(20))
        print('-'*20)

        self.name = input('Enter name: ')
        password = input('Enter password: ')
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute('SELECT count(*) FROM users;')
                id = curs.fetchall()[0][0]
                curs.execute(f"INSERT INTO users VALUES ({id+1}, '{self.name}', ENCODE('{password}', 'hex'))")

    #adding new character to table characters and weapon to table weapons
    def new_character(self) -> None:
        while True:
            #character
            print('-'*20)
            print('Choose character: ')
            print('1. Warrior')
            print('2. Wizard')
            print('3. Archer')
            print("")
            try:
                self.choose_character = int(input('Choose: '))
                print('-'*20)
                if 1<= self.choose_character <= 3:
                    break
                else:
                    print("")
                    print('The number is out of range!')
                    print("")
                    time.sleep(1) 
                    continue
            except ValueError:
                print("")
                print('Enter a number!')
                print("")
                time.sleep(1)
            

        while True:
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
                
            
            try:
                self.choose_weapon = int(input('Choose: '))
                if self.choose_character == 1 and 1<= self.choose_weapon <=3:
                    break
                elif self.choose_character == 2 and 3<= self.choose_weapon <=6:
                    break
                elif self.choose_character == 3 and 6<= self.choose_weapon <=9:
                    break
                else:
                    print("")
                    print('The number is out of range!')
                    print("")
                    time.sleep(1) 
                    continue
                
            except ValueError:
                print("")
                print('Enter a number!')
                print("")
                time.sleep(1)

    #user login
    def login(self) -> None:
        while True:
            print('-'*20)
            print('Login'.center(20))
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
                while True:
                    answer = input('Do you wanna register? (Y/N) ')
                    if answer.upper() == 'Y':
                        self.new_user()
                        self.new_character()
                        self.add_to_main()
                        print('')
                        print('Sign in now')
                        break
                    elif answer.upper() == 'N':
                        break
                    else:
                        print("")
                        print('You can only choose between yes and no!')
                        time.sleep(1)

    #adding data to main table
    def add_to_main(self) -> None:
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
    def user_character(self) -> None:
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(f"SELECT ch.name, w.name FROM characters as ch, weapons as w, main as m, users as u WHERE m.id_character=ch.id and m.id_weapon=w.id and m.id_user=u.id and u.name='{self.name}';")
                characters = curs.fetchall()

                while True:
                    print('1. Choose already created hero')
                    print('2. Create new hero')
                    print("")
                    try:
                        answer = int(input('Choose: '))
                    except ValueError:
                        print('Enter a number!')

                    if answer == 1:
                        if len(characters) != 0:
                            print("")
                            for i, character in enumerate(characters):
                                weapons = character[1].split("_")
                                try:
                                    print(f'{i+1}. {character[0]} with {weapons[0].capitalize()} {weapons[1]}') 
                                except IndexError:
                                    print(f'{i+1}. {character[0]} with {weapons[0].capitalize()}') 

                            print("")
                            while True:
                                try:
                                    id_charcter = int(input('Choose your hero: '))
                                    break
                                except ValueError:
                                    print('Enter a number!')
                                    time.sleep(1)
                            self.character = (characters[id_charcter-1][0])
                            self.weapon = (characters[id_charcter-1][1])
                            break

                        else:
                            print("")
                            print("You don't have any hero!")
                            print("")
                            time.sleep(1)

                    else:
                        self.new_character()
                        self.add_to_main()
                        print("")
                        print('New hero created!')
                        time.sleep(1)
                
                
    #getting stats of user character
    def user_stats(self) -> tuple[tuple, tuple]:
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(f"SELECT * FROM characters WHERE name='{self.character}'")
                stats_character = curs.fetchall()[0]

                curs.execute(f"SELECT * FROM weapons WHERE name='{self.weapon}'")
                stats_weapon = curs.fetchall()[0]

        return stats_character, stats_weapon

    #executing query from db
    def execute(self, query) -> list[tuple]:
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(query)
                try:
                    return curs.fetchall()
                except sql.ProgrammingError:
                    return None

    #getting name user
    def get_name(self) -> str:
        return self.name

    #closing connection
    def close(self) -> any:
        return self.conn.close()