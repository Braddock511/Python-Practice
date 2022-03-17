import time
import pymysql as sql
from Characters import Character
from Weapons import Weapon
ch = Character()
we = Weapon()

con = sql.Connect(host='127.0.0.1', unix_socket='', user='root', password='', db='dbgame') 
cur = con.cursor() 

class Game():
    character = None
    weapon = None
    gold = 0
    def __init__(self):
        print('Welcome in Adventure Game!')
        print("")
        print('Choose character: ')
        print('1. Warrior')
        print('2. Wizard')
        print('3. Archer')
        print("")
        choose_character = int(input('Choose: '))
        print('-'*20)

        if choose_character==1:
            self.character = ch.warrior()
            print('Choose weapon: ')
            print('1. Sword')
            print('2. Axe')
            print('3. Spear')
            print("")
            choose_weapon = int(input('Choose: '))
            if choose_weapon==1:
                self.weapon = we.sword()
            if choose_weapon==2:
                self.weapon = we.axe()
            if choose_weapon==3:
                self.weapon = we.spear()

        if choose_character==2:
            self.character = ch.wizard()
            print('Choose weapon: ')
            print('1. Fire wand')
            print('2. Wind wand')
            print('3. Lighting wand')
            print("")
            choose_weapon = int(input('Choose: '))
            if choose_weapon==1:
                self.weapon = we.fire_wand()
            if choose_weapon==2:
                self.weapon = we.wind_wand()
            if choose_weapon==3:
                self.weapon = we.lighting_wand()

        if choose_character==3:
            self.character = ch.archer()
            print('Choose weapon: ')
            print('1. Short bow')
            print('2. Long bow')
            print('3. Crossbow')
            print("")
            choose_weapon = int(input('Choose: '))
            if choose_weapon==1:
                self.weapon = we.short_bow()
            if choose_weapon==2:
                self.weapon = we.long_bow()
            if choose_weapon==3:
                self.weapon = we.crossbow()

        print('-'*20)
        print('So you picked your hero, now you can go to conquer new land!')
        time.sleep(2.5)
        print("But you can't, because...")
        time.sleep(2)
        print('You are poor and you have 0 gold, so you need take a contract on a monster!')
        time.sleep(2.5)
        print('-'*20)
        input('Press enter to continue ')

        print('You are in village, you see board with orders')
        time.sleep(2.5)
        print('You have 2 options: ')
        time.sleep(1)
        print("")
        print('1. Take a contract in which you have to solve riddle in village')
        print('2. Take a contract in which you have to regain treasure of rich resident from village')
        print('-'*20)
        answer = int(input('Choose: '))
        
        
    if __name__ == '__main__':
        pass

game = Game()

#stworzyć bazę danych